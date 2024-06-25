from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_integration_structure(node_id):
    true = True
    false = False
    integration = {
      "id": "{}".format(node_id),
      "position": {
        "x": 0,
        "y": 0
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Integration",
        "version": 1,
        "name": "IntegrationNode",
        "type": "IntegrationNode",
        "baseClasses": [
          "IntegrationNode"
        ],
        "category": "Main Nodes",
        "description": "Integration with JIRA.",
        "inputParams": [
          {
            "label": "JIRA URL",
            "name": "JIRA_URL",
            "type": "string",
            "description": "The URL of the JIRA server.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-JIRA_URL-string".format(node_id)
          },
          {
            "label": "Project Key",
            "name": "projectkey",
            "type": "string",
            "description": "The key of the project in JIRA.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-projectkey-string".format(node_id)
          },
          {
            "label": "Authentication",
            "name": "authentication",
            "type": "password",
            "description": "The authentication token for the JIRA server.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-authentication-password".format(node_id)
          }
        ],
        "inputAnchors": [],
        "inputs": {
          "JIRA_URL": "",
          "projectkey": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-IntegrationNode-IntegrationNode".format(node_id),
            "name": "IntegrationNode",
            "label": "IntegrationNode",
            "description": "Integration with JIRA.",
            "type": "IntegrationNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 253,
      "positionAbsolute": {
        "x": 0,
        "y": 0
      },
      "selected": false
    }
    return integration

def reduced_integration(node_id, data, edge_list):
    integration = {
      "node": "IntegrationNode",
      "node_id": "{}".format(node_id),
      "data": {
        "JIRA_URL": "{}".format(data["JIRA_URL"]),
        "projectkey": "{}".format(data["projectkey"]),
      },
      "next_node": get_next_node_id(node_id, edge_list)
    }
    return integration