import csv
import requests

# Define the headers for the request
headers = {'Accept': 'application/vnd.github+json'}

# Prompt the user for the organization name
org_name = input("Enter the name of the GitHub organization: ")

# Define the initial URL for the API request
url = f'https://api.github.com/orgs/{org_name}/repos'

# Initialize a list to store the repository data
repo_data = []

while url:
    # Send a GET request to the GitHub API to retrieve the list of repositories for the organization
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Retrieve the JSON data from the response
        repo_data += response.json()
        
        # Check if there are more pages of results
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None
    else:
        # If the request was not successful, print an error message and break out of the loop
        print(f"Request failed with status code {response.status_code}")
        break

# Define the name of the output CSV file
output_file = f"{org_name}_repos.csv"

# Write the data to a CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'description', 'url'])
    for repo in repo_data:
        repo_url = repo['html_url'].replace("https://", "")
        writer.writerow([repo['name'], repo['description'], repo_url])
