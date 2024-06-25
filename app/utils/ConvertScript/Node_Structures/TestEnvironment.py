from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_test_environment_structure(node_id):
    true = True
    false = False
    test_environment = {
      "id": "{}".format(node_id),
      "position": {
        "x": 400,
        "y": -int(node_id) * 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Test Environment",
        "version": 1,
        "name": "TestEnvironmentNode",
        "type": "TestEnvironmentNode",
        "baseClasses": [
          "TestEnvironmentNode"
        ],
        "category": "Main Nodes",
        "description": "Isolated system replica for running tests without impacting production.",
        "inputParams": [
          {
            "label": "Name",
            "name": "name",
            "type": "string",
            "id": "{}-input-name-string".format(node_id)
          },
          {
            "label": "URL",
            "name": "url",
            "type": "string",
            "description": "URL of the test environment.",
            "optional": true,
            "id": "{}-input-url-string".format(node_id)
          },
          {
            "label": "Database",
            "name": "database",
            "type": "string",
            "description": "Database used for the tests.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-database-string".format(node_id)
          },
          {
            "label": "Credentials",
            "name": "credentials",
            "type": "string",
            "description": "Credentials for the test environment.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-credentials-string".format(node_id)
          },
          {
            "label": "Tools",
            "name": "tools",
            "type": "string",
            "description": "Tools used for the tests.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-tools-string".format(node_id)
          }
        ],
        "inputAnchors": [],
        "inputs": {
          "name": "",
          "url": "",
          "database": "",
          "credentials": "",
          "tools": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-TestEnvironmentNode-TestEnvironmentNode".format(node_id),
            "name": "TestEnvironmentNode",
            "label": "TestEnvironmentNode",
            "description": "Isolated system replica for running tests without impacting production.",
            "type": "TestEnvironmentNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 430,
      "selected": false,
      "positionAbsolute": {
        "x": 400,
        "y": -int(node_id) * 450
      },
      "dragging": false
    }
    return test_environment



def reduced_test_environment(node_id, data, edge_list):
    test_environment = {
        "node": "TestEnvironmentNode",
        "node_id": "{}".format(node_id),
        "data": {
          "name": "{}".format(data["name"]),
          "url": "{}".format(data["url"]),
          "database": "{}".format(data["database"]),
          "credentials": "{}".format(data["credentials"]),
          "tools": "{}".format(data["tools"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return test_environment