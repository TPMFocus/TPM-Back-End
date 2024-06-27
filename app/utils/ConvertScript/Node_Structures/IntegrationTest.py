from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_integration_test_structure(node_id):
    true = True
    false = False
    integration_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 1600,
        "y": 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Integration Test Case",
        "version": 1,
        "name": "IntegrationTestNode",
        "type": "IntegrationTestNode",
        "baseClasses": [
          "IntegrationTestNode"
        ],
        "category": "Integration Test Nodes",
        "description": "Test verifying how multiple software modules or systems work together as a whole.",
        "inputParams": [
          {
            "label": "Title",
            "name": "title",
            "type": "string",
            "id": "{}-input-title-string".format(node_id)
          },
          {
            "label": "Description",
            "name": "description",
            "type": "string",
            "rows": 4,
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-description-string".format(node_id)
          },
          {
            "label": "Priority",
            "name": "priority",
            "type": "options",
            "options": [
              {
                "label": "High",
                "name": "High"
              },
              {
                "label": "Medium",
                "name": "Medium"
              },
              {
                "label": "Low",
                "name": "Low"
              }
            ],
            "optional": true,
            "id": "{}-input-priority-options".format(node_id)
          },
          {
            "label": "Tags",
            "name": "tags",
            "type": "string",
            "optional": true,
            "id": "{}-input-tags-string".format(node_id)
          },
          {
            "label": "Target Layer",
            "name": "targetLayer",
            "type": "options",
            "options": [
              {
                "label": "Front-End",
                "name": "Front-End"
              },
              {
                "label": "Back-End",
                "name": "Back-End"
              }
            ],
            "optional": true,
            "id": "{}-input-targetLayer-options".format(node_id)
          }
        ],
        "inputAnchors": [
          {
            "label": "",
            "name": "input",
            "type": "TestSuiteNode",
            "optional": true,
            "id": "{}-input-input-TestSuiteNode".format(node_id)
          }
        ],
        "inputs": {
          "input": "{{TestSuiteNode_0.data.instance}}",
          "title": "",
          "description": "",
          "priority": "",
          "tags": "",
          "targetLayer": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-IntegrationTestNode-IntegrationTestNode".format(node_id),
            "name": "IntegrationTestNode",
            "label": "IntegrationTestNode",
            "description": "Test verifying how multiple software modules or systems work together as a whole.",
            "type": "IntegrationTestNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 654,
      "selected": false,
      "dragging": false,
      "positionAbsolute": {
        "x": 1600,
        "y": 450
      }
    }
    return integration_test


def reduced_integration_test(node_id, data, edge_list):
    integration_test = {
        "node": "IntegrationTestNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data["title"]),
          "description": "{}".format(data["description"]),
          "priority": "{}".format(data["priority"]),
          "tags": "{}".format(data["tags"]),
          "targetLayer": "{}".format(data["targetLayer"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return integration_test