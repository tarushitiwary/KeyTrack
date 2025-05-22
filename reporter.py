import os
from jinja2 import Environment, FileSystemLoader

LOG_FILE = "logs/log.txt"
TEMPLATE_DIR = "templates"
OUTPUT_FILE = "report.html"

def generate_html_report():
    if not os.path.exists(LOG_FILE):
        print(f"[❌] Log file not found: {LOG_FILE}")
        return

    with open(LOG_FILE, encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if "|" in line]

    if not lines:
        print("[⚠️] Log file is empty or improperly formatted.")
        return

    entries = [line.split(" | ") for line in lines]

    if not os.path.exists(os.path.join(TEMPLATE_DIR, "report.html")):
        print(f"[❌] Template not found in '{TEMPLATE_DIR}' folder.")
        return

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("report.html")

    html = template.render(entries=entries)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[✅] Report generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_html_report()
