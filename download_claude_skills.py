
import os
import requests

# Configuration
CLAUDE_REPO_OWNER = "anthropics"
CLAUDE_REPO_NAME = "claude-code"
GITHUB_REF = "2923bc87d10da4fda57570313f2abbc5b457fed1"
BASE_RAW_URL = f"https://raw.githubusercontent.com/{CLAUDE_REPO_OWNER}/{CLAUDE_REPO_NAME}/{GITHUB_REF}"
LOCAL_BASE_DIR = "f:/Documentos/GitHub/WebWAM/skills/claude-code"

SKILLS_PATHS = [
    "plugins/hookify/skills/writing-rules/SKILL.md",
    "plugins/plugin-dev/skills/command-development/SKILL.md",
    "plugins/plugin-dev/skills/plugin-structure/SKILL.md",
    "plugins/plugin-dev/skills/mcp-integration/SKILL.md",
    "plugins/plugin-dev/skills/agent-development/SKILL.md",
    "plugins/plugin-dev/skills/plugin-settings/SKILL.md",
    "plugins/plugin-dev/skills/skill-development/SKILL.md",
    "plugins/frontend-design/skills/frontend-design/SKILL.md",
    "plugins/claude-opus-4-5-migration/skills/claude-opus-4-5-migration/SKILL.md",
    "plugins/plugin-dev/skills/hook-development/SKILL.md"
]

def download_skill(github_path):
    # Determine local folder name
    parts = github_path.split("/")
    # Path is plugins/<plugin>/skills/<skill-name>/SKILL.md
    if len(parts) >= 4 and parts[2] == "skills":
        skill_name = parts[3]
    else:
        skill_name = parts[-2]
    
    local_dir = os.path.join(LOCAL_BASE_DIR, skill_name)
    local_path = os.path.join(local_dir, "SKILL.md")
    
    url = f"{BASE_RAW_URL}/{github_path}"
    print(f"Downloading {url} -> {local_path}")
    
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(local_dir, exist_ok=True)
        with open(local_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Successfully installed {skill_name}")
    else:
        print(f"Failed to download {url}: {response.status_code}")

def main():
    print("Starting Claude Code skills installation...")
    for path in SKILLS_PATHS:
        download_skill(path)
    print("Finished.")

if __name__ == "__main__":
    main()
