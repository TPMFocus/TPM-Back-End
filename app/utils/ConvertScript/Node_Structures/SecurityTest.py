from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_security_test_structure(node_id):
    true = True
    false = False
    security_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 1600,
        "y": 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Security Test Case",
        "version": 1,
        "name": "SecurityTestNode",
        "type": "SecurityTestNode",
        "baseClasses": [
          "SecurityTestNode"
        ],
        "category": "Test Case Nodes",
        "description": "Assessment of a system's vulnerability to unauthorized access, data breaches, or other malicious attacks.",
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
            "label": "Type",
            "name": "type",
            "type": "options",
            "options": [
              {
                "label": "Penetration Testing",
                "name": "Penetration Testing"
              },
              {
                "label": "Vulnerability Scanning",
                "name": "Vulnerability Scanning"
              },
              {
                "label": "Other",
                "name": "Other"
              }
            ],
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-type-options".format(node_id)
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
          "type": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-SecurityTestNode-SecurityTestNode".format(node_id),
            "name": "SecurityTestNode",
            "label": "SecurityTestNode",
            "description": "Assessment of a system's vulnerability to unauthorized access, data breaches, or other malicious attacks.",
            "type": "SecurityTestNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 735,
      "positionAbsolute": {
        "x": 1600,
        "y": 450
      },
      "selected": false
    }
    return security_test


def reduced_security_test(node_id, data, edge_list):
    security_test = {
        "node": "SecurityTestNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data["title"]),
          "description": "{}".format(data["description"]),
          "priority": "{}".format(data["priority"]),
          "tags": "{}".format(data["tags"]),
          "type": "{}".format(data["type"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return security_test
    