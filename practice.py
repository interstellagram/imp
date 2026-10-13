import requests
import base64

# GitHub details
GITHUB_USERNAME = "your_username"
REPO_NAME = "Spoon-Knife"
FILE_PATH = "hello.py"
BRANCH = "feature/my-first-change"
TOKEN = "your_github_personal_access_token"

# Content to upload
content = '''print("Hello GitHub!")
print("Uploaded using Python")
'''

# GitHub API URL
url = (
    f"https://api.github.com/repos/"
    f"{GITHUB_USERNAME}/{REPO_NAME}/contents/{FILE_PATH}"
)

# Encode file content
encoded_content = base64.b64encode(
    content.encode("utf-8")
).decode("utf-8")

# Request headers
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Upload details
data = {
    "message": "Upload Python file using API",
    "content": encoded_content,
    "branch": BRANCH
}

# Upload file
response = requests.put(url, headers=headers, json=data)

if response.status_code in (200, 201):
    print("File uploaded successfully!")
    print(response.json()["content"]["html_url"])
else:
    print("Upload failed:", response.status_code)
    print(response.json())