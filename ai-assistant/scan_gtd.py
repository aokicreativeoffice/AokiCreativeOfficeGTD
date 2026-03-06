import os
from openai import OpenAI
from datetime import date

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../gtd"))

def read_folder(path, limit=5):
    texts = []
    for root, _, files in os.walk(path):
        for f in files[:limit]:
            if f.endswith(".md"):
                with open(os.path.join(root, f), encoding="utf-8") as fp:
                    texts.append(fp.read())
    return "\n\n".join(texts)

inbox = read_folder(os.path.join(BASE, "inbox"))
projects = read_folder(os.path.join(BASE, "projects"))
actions = read_folder(os.path.join(BASE, "next-actions"))

with open(os.path.join(os.path.dirname(__file__), "prompt.txt"), encoding="utf-8") as f:
    system_prompt = f.read()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"""
[inbox]
{inbox}

[projects]
{projects}

[next-actions]
{actions}
"""}
    ]
)

task = response.choices[0].message.content

out_dir = os.path.join(BASE, "next-actions", "dev")
os.makedirs(out_dir, exist_ok=True)

fname = f"auto_{date.today()}.md"
with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
    f.write(task)

print("Generated:", fname)