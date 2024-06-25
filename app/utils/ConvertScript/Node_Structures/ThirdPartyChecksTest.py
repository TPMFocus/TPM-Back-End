from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_third_party_checks_test_structure(node_id):
    true = True
    false = False
    third_party_checks = {
      "id": "{}".format(node_id),
      "position": {
        "x": 1600,
        "y": -int(node_id) * 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Third Party Checks",
        "version": 1,
        "name": "ThirdPartyChecksNode",
        "type": "ThirdPartyChecksNode",
        "baseClasses": [
          "ThirdPartyChecksNode"
        ],
        "category": "Test Case Nodes",
        "description": "Verification of integrations with external systems or services.",
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
            "type": "string",
            "description": "Type of the third party check.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-type-string".format(node_id)
          },
          {
            "label": "Tools",
            "name": "tools",
            "type": "string",
            "description": "Tools used for the checks.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-tools-string".format(node_id)
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
          "type": "",
          "tools": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-ThirdPartyChecksNode-ThirdPartyChecksNode".format(node_id),
            "name": "ThirdPartyChecksNode",
            "label": "ThirdPartyChecksNode",
            "description": "Verification of integrations with external systems or services.",
            "type": "ThirdPartyChecksNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 735,
      "selected": false,
      "positionAbsolute": {
        "x": 1600,
        "y": -int(node_id) * 450
      },
      "dragging": false
    }
    return third_party_checks

def reduced_third_party_checks_test_structure(node_id, data, edge_list):
    third_party_checks = {
        "node": "ThirdPartyChecksNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data["title"]),
          "description": "{}".format(data["description"]),
          "priority": "{}".format(data["priority"]),
          "tags": "{}".format(data["tags"]),
          "type": "{}".format(data["type"]),
          "tools": "{}".format(data["tools"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return third_party_checks