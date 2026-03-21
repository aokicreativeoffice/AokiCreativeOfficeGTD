import express from "express";
import OpenAI from "openai";
import { createClient } from "@supabase/supabase-js";
import dotenv from "dotenv";

dotenv.config();

const app = express();
app.use(express.json());

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_KEY
);

// ノート生成
async function generateNote(question) {
  const prompt = `
以下の構造でノートを生成せよ：

- Concept
- Structure
- Mechanism
- Relation（5個以上）
- Pattern
- Implication

relationは以下のみ：
is_a, is_instance_of, part_of, depends_on, leads_to, causes, influences, contrasts_with

JSON形式で出力：
{
  "title": "",
  "type": "case",
  "content": "",
  "relations": [
    {"target": "", "relation": ""}
  ]
}

質問:
${question}
`;

  const res = await openai.chat.completions.create({
    model: "gpt-5.3",
    messages: [{ role: "user", content: prompt }],
  });

  return JSON.parse(res.choices[0].message.content);
}

// embedding
async function embed(text) {
  const res = await openai.embeddings.create({
    model: "text-embedding-3-small",
    input: text,
  });
  return res.data[0].embedding;
}

// 保存
async function saveNode(note) {
  const embedding = await embed(note.content);

  const { data } = await supabase
    .from("nodes")
    .insert({
      title: note.title,
      type: note.type,
      content: note.content,
      embedding: embedding,
    })
    .select();

  return data[0];
}

// edge保存
async function saveEdges(nodeId, relations) {
  for (const r of relations) {
    const { data: target } = await supabase
      .from("nodes")
      .select("id")
      .eq("title", r.target)
      .maybeSingle();

    if (target) {
      await supabase.from("edges").insert({
        source_id: nodeId,
        target_id: target.id,
        relation: r.relation,
      });
    }
  }
}

// API
app.post("/generate", async (req, res) => {
  try {
    const { question } = req.body;

    const note = await generateNote(question);
    const node = await saveNode(note);
    await saveEdges(node.id, note.relations);

    res.json({ success: true, node });
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: e.message });
  }
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});