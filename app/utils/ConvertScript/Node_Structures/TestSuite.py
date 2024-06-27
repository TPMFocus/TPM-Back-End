from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_test_suite_structure(node_id):
    true = True
    false = False
    test_suite = {
      "id": "{}".format(node_id),
      "position": {
        "x": 1200,
        "y": 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Test Suite",
        "version": 1,
        "name": "TestSuiteNode",
        "type": "TestSuiteNode",
        "baseClasses": [
          "TestSuiteNode"
        ],
        "category": "Main Nodes",
        "description": "Collection of organized test cases designed to be run together for a specific functionality or feature.",
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
            "label": "Exit Criteria",
            "name": "exitCriteria",
            "type": "string",
            "rows": 4,
            "description": "Conditions that must be met before the test suite can be considered complete.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-exitCriteria-string".format(node_id)
          }
        ],
        "inputAnchors": [
          {
            "label": "",
            "name": "input",
            "type": "TestPlanNode",
            "optional": true,
            "id": "{}-input-input-TestPlanNode".format(node_id)
          }
        ],
        "inputs": {
          "input": "{{TestPlanNode_0.data.instance}}",
          "title": "",
          "description": "",
          "exitCriteria": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-TestSuiteNode-TestSuiteNode".format(node_id),
            "name": "TestSuiteNode",
            "label": "TestSuiteNode",
            "description": "Collection of organized test cases designed to be run together for a specific functionality or feature.",
            "type": "TestSuiteNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 540,
      "selected": false,
      "positionAbsolute": {
        "x": 1200,
        "y": 450
      },
      "dragging": false
    }
    return test_suite

def reduced_test_suite(node_id, data, edge_list):
    test_suite = {
        "node": "TestSuiteNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data["title"]),
          "description": "{}".format(data["description"]),
          "exitCriteria": "{}".format(data["exitCriteria"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return test_suite