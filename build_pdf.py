import subprocess
import glob

files = sorted(glob.glob("*.md"))

cmd = ["pandoc"] + files + ["-o", "vault_print.pdf"]

subprocess.run(cmd)