import json
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, request, jsonify, render_template
import threading
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
jira_url = ""
username = ""
api_token = ""
nodes_json_file = ''

class JiraIntegration:
    def __init__(self, jira_url, username, api_token):
        self.jira_url = jira_url
        self.username = username
        self.api_token = api_token
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def get_all_projects(self):
        url = f"{self.jira_url}/rest/api/3/project/search"
        response = requests.get(url, headers=self.headers, auth=HTTPBasicAuth(self.username, self.api_token))

        if response.status_code == 200:
            projects = response.json()["values"]
            return projects, 200
        else:
            return None, response.status_code

    def get_all_issue_type_schemes(self):
        url = f"{self.jira_url}/rest/api/3/issuetypescheme"
        response = requests.get(url, headers=self.headers, auth=HTTPBasicAuth(self.username, self.api_token))

        if response.status_code == 200:
            schemes = response.json()["values"]
            return schemes, 200
        else:
            return None, response.status_code

    def get_issue_type_scheme_id(self, issue_type_scheme_name):
        url = f"{self.jira_url}/rest/api/3/issuetypescheme"
        response = requests.get(url, headers=self.headers, auth=HTTPBasicAuth(self.username, self.api_token))

        if response.status_code == 200:
            schemes = response.json()["values"]
            for scheme in schemes:
                if scheme['name'] == issue_type_scheme_name:
                    return scheme['id']
            return None
        else:
            return None

    def create_issue_type(self, issue_type_name, issue_type_scheme_name):
        url = f"{self.jira_url}/rest/api/3/issuetype"
        response = requests.get(url, headers=self.headers, auth=HTTPBasicAuth(self.username, self.api_token))

        issue_type_id = None
        for issue_type in response.json():
            if issue_type['name'] == issue_type_name:
                issue_type_id = issue_type['id']
                break

        if issue_type_id is None:
            create_url = f"{self.jira_url}/rest/api/3/issuetype"
            payload = {
                "name": issue_type_name,
                "description": f"This is a custom issue type '{issue_type_name}' created via API.",
                "type": "standard"
            }

            create_response = requests.post(
                create_url,
                headers=self.headers,
                auth=HTTPBasicAuth(self.username, self.api_token),
                json=payload
            )

            if create_response.status_code == 201:
                issue_type_id = create_response.json()["id"]
            else:
                return None
        issue_type_scheme_id = self.get_issue_type_scheme_id(issue_type_scheme_name)
        if issue_type_scheme_id is None:
            return None
        
        self.add_issue_type_to_scheme(issue_type_id, issue_type_scheme_id)
        return issue_type_id

    def add_issue_type_to_scheme(self, issue_type_id, issue_type_scheme_id):
        url = f"{self.jira_url}/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype"
        payload = {
            "issueTypeIds": [issue_type_id]
        }

        response = requests.put(
            url,
            headers=self.headers,
            auth=HTTPBasicAuth(self.username, self.api_token),
            json=payload
        )

    def create_jira_task(self, title, issue_type_name, issue_type_scheme_name, project_key):
        issue_type_id = self.create_issue_type(issue_type_name, issue_type_scheme_name)

        if issue_type_id is None:
            return None

        url = f"{self.jira_url}/rest/api/3/issue"
        payload = {
            "fields": {
                "project": {
                    "key": project_key
                },
                "summary": title,
                "issuetype": {
                    "id": issue_type_id  
                }
            }
        }

        response = requests.post(
            url,
            headers=self.headers,
            auth=HTTPBasicAuth(self.username, self.api_token),
            json=payload
        )

        if response.status_code == 201:
            issue_key = response.json()["key"]
            return issue_key  
        else:
            return None

    def create_issue_link(self, source_issue_key, destination_issue_key, link_type):
        url = f"{self.jira_url}/rest/api/3/issueLink"
        payload = {
            "type": {
                "name": link_type
            },
            "inwardIssue": {
                "key": source_issue_key
            },
            "outwardIssue": {
                "key": destination_issue_key
            }
        }

        response = requests.post(
            url,
            headers=self.headers,
            auth=HTTPBasicAuth(self.username, self.api_token),
            json=payload
        )

    def process_nodes_json(self, nodes_json_file, issue_type_scheme_name, project_key):
        with open(nodes_json_file, 'r') as f:
            data = json.load(f)

        task_keys = []

        for node in data["nodes"]:
            if "data" in node and "label" in node["data"]:
                title = node["data"]["label"]
                issue_type_name = title
                task_key = self.create_jira_task(title, issue_type_name, issue_type_scheme_name, project_key)
                if task_key:
                    task_keys.append(task_key)

        for i in range(len(task_keys)-1):
            self.create_issue_link(task_keys[i], task_keys[i+1], "Relates")

def run_jira_integration(jira_integration, issue_type_scheme_name, project_key):
    jira_integration.process_nodes_json(nodes_json_file, issue_type_scheme_name, project_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-projects', methods=['POST'])
def get_projects():
    data = request.get_json()
    jira_integration = JiraIntegration(data['jira_url'], data['username'], data['api_token'])
    projects, status_code = jira_integration.get_all_projects()
    if projects is not None:
        return jsonify(projects), status_code
    else:
        return jsonify({"error": "Failed to fetch projects."}), status_code

@app.route('/get-schemes', methods=['POST'])
def get_schemes():
    data = request.get_json()
    jira_integration = JiraIntegration(data['jira_url'], data['username'], data['api_token'])
    schemes, status_code = jira_integration.get_all_issue_type_schemes()
    if schemes is not None:
        return jsonify(schemes), status_code
    else:
        return jsonify({"error": "Failed to fetch issue type schemes."}), status_code

@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    jira_integration = JiraIntegration(jira_url, username, api_token)
    issue_type_scheme_name = data['issue_type_scheme_name']
    project_key = data['project_key']
    threading.Thread(target=run_jira_integration, args=(jira_integration, issue_type_scheme_name, project_key)).start()
    return jsonify({"message": "Jira integration process started"}), 200

if __name__ == "__main__":
    app.run(port=5001)
