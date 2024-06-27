from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_frontend_integration_test_structure(node_id):
    true = True
    false = False
    frontend_integration_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 2400,
        "y": 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Front End Integration Test Case",
        "version": 1,
        "name": "FrontEndIntegrationTestNode",
        "type": "FrontEndIntegrationTestNode",
        "baseClasses": [
          "FrontEndIntegrationTestNode"
        ],
        "category": "Integration Test Nodes",
        "description": "Test verifying interaction between UI elements and their backend data flow.",
        "inputParams": [
          {
            "label": "Integration Scope",
            "name": "IntegrationScope",
            "type": "string",
            "description": "Specific components and functionalities within the frontend that interact with backend services.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-IntegrationScope-string".format(node_id)
          },
          {
            "label": "Front End Technology",
            "name": "FrontEndTechnology",
            "type": "string",
            "description": "Tools and frameworks used to build the user interface (HTML, CSS, JavaScript libraries) under test.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-FrontEndTechnology-string".format(node_id)
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
          "FrontEndTechnology": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-FrontEndIntegrationTestNode-FrontEndIntegrationTestNode".format(node_id),
            "name": "FrontEndIntegrationTestNode",
            "label": "FrontEndIntegrationTestNode",
            "description": "Test verifying interaction between UI elements and their backend data flow.",
            "type": "FrontEndIntegrationTestNode"
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
        "y": 450
      },
      "dragging": false
    }
    return frontend_integration_test


def reduced_frontend_integration_test(node_id, data):
    frontend_integration_test = {
        "node": "FrontEndIntegrationTestNode",
        "node_id": "{}".format(node_id),
        "data": {
          "IntegrationScope": "{}".format(data["IntegrationScope"]),
          "FrontEndTechnology": "{}".format(data["FrontEndTechnology"])
        }
    }
    return frontend_integration_test