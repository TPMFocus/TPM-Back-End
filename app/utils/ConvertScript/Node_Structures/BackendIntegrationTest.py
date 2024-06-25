from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_backend_integration_test_structure(node_id):
    true = True
    false = False
    backend_integration_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 2400,
        "y": -int(node_id) * 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Back End Integration Test Case",
        "version": 1,
        "name": "BackEndIntegrationTestNode",
        "type": "BackEndIntegrationTestNode",
        "baseClasses": [
          "BackEndIntegrationTestNode"
        ],
        "category": "Integration Test Nodes",
        "description": "Scripts that check how different backend parts interact and function together as a system.",
        "inputParams": [
          {
            "label": "Integration Scope",
            "name": "IntegrationScope",
            "type": "string",
            "description": "The breadth of backend components an automated test orchestrates to verify a feature's functionality.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-IntegrationScope-string".format(node_id)
          },
          {
            "label": "Back End Technology",
            "name": "BackEndTechnology",
            "type": "string",
            "description": "(e.g., Python, Django, PostgreSQL)",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-BackEndTechnology-string".format(node_id)
          }
        ],
        "inputAnchors": [
          {
            "label": "",
            "name": "input",
            "type": "IntegrationTestNode",
            "optional": true,
            "id": "{}-input-input-IntegrationTestNode".format(node_id)
          }
        ],
        "inputs": {
          "input": "{{IntegrationTestNode_0.data.instance}}",
          "IntegrationScope": "",
          "BackEndTechnology": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-BackEndIntegrationTestNode-BackEndIntegrationTestNode".format(node_id),
            "name": "BackEndIntegrationTestNode",
            "label": "BackEndIntegrationTestNode",
            "description": "Scripts that check how different backend parts interact and function together as a system.",
            "type": "BackEndIntegrationTestNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 265,
      "selected": false,
      "positionAbsolute": {
        "x": 2400,
        "y": -int(node_id) * 450
      },
      "dragging": false
    }
    return backend_integration_test



def reduced_backend_integration_test(node_id, data, edge_list):
    backend_integration_test = {
        "node": "BackEndIntegrationTestNode",
        "node_id": "{}".format(node_id),
        "data": {
          "IntegrationScope": "{}".format(data["IntegrationScope"]),
          "BackEndTechnology": "{}".format(data["BackEndTechnology"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return backend_integration_test