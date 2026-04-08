
import os
import requests
import re

# Configuration
REPO_OWNER = "wilfredoabadmt"
REPO_NAME = "marketingskills"
GITHUB_REF = "90a7e84d0ef924b8116bd9fef8bef137ee5e18f9"
BASE_URL = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{GITHUB_REF}"
LOCAL_BASE_DIR = "f:/Documentos/GitHub/WebWAM/skills/marketingskills"

def get_skill_list():
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/skills?ref={GITHUB_REF}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return [item['name'] for item in response.json() if item['type'] == 'dir']
    return []

def download_file(github_path, local_path):
    url = f"{BASE_URL}/{github_path}"
    print(f"Downloading {url} -> {local_path}")
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        return response.text
    return None

def process_skill(skill_name):
    skill_dir = os.path.join(LOCAL_BASE_DIR, skill_name)
    github_skill_path = f"skills/{skill_name}/SKILL.md"
    local_skill_path = os.path.join(skill_dir, "SKILL.md")
    
    content = download_file(github_skill_path, local_skill_path)
    if content:
        # Find references
        refs = re.findall(r'\[.*?\]\((references/.*?\.md)\)', content)
        for ref in refs:
            ref_github_path = f"skills/{skill_name}/{ref}"
            ref_local_path = os.path.join(skill_dir, ref)
            download_file(ref_github_path, ref_local_path)

def main():
    skills = get_skill_list()
    print(f"Found {len(skills)} skills.")
    for skill in skills:
        process_skill(skill)

if __name__ == "__main__":
    main()
