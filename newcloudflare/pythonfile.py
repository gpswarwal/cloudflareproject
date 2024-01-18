import requests


# Replace with your Cloudflare API token and account ID
api_token = "bVGNh6VAmVGMbICG5jPIoHYkwgP6gYJS419r30Il"
account_id = "06761dbd3d3295eb63349ea3ae20ea8a"

# Cloudflare Pages endpoint
pages_endpoint = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects"

# Application data
application_data = {
    "name": "deploytoken.pages.dev",
    "files": [
        {
            "file": "C:\Users\singhgurpreet3\Downloads\newcloudflare\index.html",  # Path to your HTML file
            "branch": "main",
        },
    ],
    "production_branch": "main",
}

# Headers with Cloudflare API token
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json",
}

# Make a POST request to create the Cloudflare Page application
response = requests.post(pages_endpoint, json=application_data, headers=headers)

# Check the response for creating the application
if response.status_code == 200:
    print("Cloudflare Page application created successfully.")
else:
    print(f"Failed to create Cloudflare Page application. Status code: {response.status_code}")
    print(response.json())