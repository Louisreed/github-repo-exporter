# GitHub Repository Exporter

This script exports the names, descriptions, and URLs of all the public repositories for a given GitHub organization to a CSV file.

## Prerequisites
- Python 3
- `requests` library
- Access to the GitHub API

## Usage
1. Clone this repository or download the script.
2. Install the `requests` library using `pip install requests`.
3. Run the script in your terminal or command prompt using `python3 github_scraper.py`.
4. Enter the name of the GitHub organization when prompted.
5. A CSV file with the name `organization_name_repos.csv` will be generated in the same directory as the script.

## Code Explanation
- The headers for the API request are defined with the `Accept` key set to `application/vnd.github+json`.
- The user is prompted to enter the name of the GitHub organization.
- The initial URL for the API request is defined using the format `https://api.github.com/orgs/organization_name/repos`.
- A GET request is sent to the GitHub API in a `while` loop to retrieve the data for all the public repositories for the organization.
- The response from the API is checked for success. If the request is not successful, an error message is printed and the loop is broken.
- If the request is successful, the JSON data is retrieved and added to the `repo_data` list.
- If there are more pages of results, the URL for the next page is retrieved. Otherwise, the loop is exited.
- The name of the output CSV file is defined using the format `organization_name_repos.csv`.
- The `repo_data` is written to the CSV file, with the header row defined as `['name', 'description', 'url']`.
- The `https://` portion of the repository URL is removed before writing it to the CSV file.
