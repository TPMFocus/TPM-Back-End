from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_unit_test_structure(node_id):
    true = True
    false = False
    unit_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 1600,
        "y": -int(node_id) * 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Unit Test Case",
        "version": 1,
        "name": "UnitTestNode",
        "type": "UnitTestNode",
        "baseClasses": [
          "UnitTestNode"
        ],
        "category": "Unit Test Nodes",
        "description": "Isolated test designed to verify the functionality of a single software unit (e.g., function, class, module) in isolation from other parts of the code.",
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
          "input": "",
          "title": "",
          "description": "",
          "priority": "",
          "tags": "",
          "targetLayer": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-UnitTestNode-UnitTestNode".format(node_id),
            "name": "UnitTestNode",
            "label": "UnitTestNode",
            "description": "Isolated test designed to verify the functionality of a single software unit (e.g., function, class, module) in isolation from other parts of the code.",
            "type": "UnitTestNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 778,
      "selected": false,
      "positionAbsolute": {
        "x": 1600,
        "y": -int(node_id) * 450
      },
      "dragging": false
    }
    return unit_test

def reduced_unit_test(node_id, data, edge_list):
    unit_test = {
        "node": "UnitTestNode",
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
    return unit_test