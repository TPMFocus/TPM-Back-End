from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_manual_test_structure(node_id):
    true = True
    false = False
    manual_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 2000,
        "y": 400
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Manual Test Case",
        "version": 1,
        "name": "ManualTestCaseNode",
        "type": "ManualTestCaseNode",
        "baseClasses": [
          "ManualTestCaseNode"
        ],
        "category": "Manual Test",
        "description": "Step-by-step instructions for a tester to verify software functionality without automation tools.",
        "inputParams": [
          {
            "label": "Title",
            "name": "title",
            "type": "string",
            "id": "{}-input-title-string".format(node_id)
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
            "label": "Preconditions",
            "name": "preconditions",
            "type": "string",
            "rows": 4,
            "description": "Requirements that must be met before a test case can be executed.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-preconditions-string".format(node_id)
          },
          {
            "label": "Postconditions",
            "name": "postconditions",
            "type": "string",
            "rows": 4,
            "description": "Expected state or outcome after a test case is executed.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-postconditions-string".format(node_id)
          },
          {
            "label": "Expected Results",
            "name": "expectedResults",
            "type": "string",
            "rows": 2,
            "description": "Expected Outcome  (or Expected Behavior)",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-expectedResults-string".format(node_id)
          },
          {
            "label": "Actual Results",
            "name": "actualResults",
            "type": "string",
            "rows": 2,
            "description": "Actual Outcome (or Observed Behavior)",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-actualResults-string".format(node_id)
          },
          {
            "label": "Test Data",
            "name": "testData",
            "type": "file",
            "description": "Sample input values used to trigger specific scenarios during testing.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-testData-file".format(node_id)
          },
          {
            "label": "Assigned Testers",
            "name": "assignedTesters",
            "type": "string",
            "rows": 2,
            "description": "Individuals designated to execute the specific test case.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-assignedTesters-string".format(node_id)
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
          "priority": "",
          "tags": "",
          "preconditions": "",
          "postconditions": "",
          "expectedResults": "",
          "actualResults": "",
          "assignedTesters": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-ManualTestCaseNode-ManualTestCaseNode".format(node_id),
            "name": "ManualTestCaseNode",
            "label": "ManualTestCaseNode",
            "description": "Step-by-step instructions for a tester to verify software functionality without automation tools.",
            "type": "ManualTestCaseNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 558,
      "positionAbsolute": {
        "x": 2000,
        "y": 400
      },
      "selected": false
    }
    return manual_test

def reduced_manual_test(node_id, data, edge_list):
    manual_test = {
        "node": "ManualTestCaseNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data["title"]),
          "priority": "{}".format(data["priority"]),
          "tags": "{}".format(data["tags"]),
          "preconditions": "{}".format(data["preconditions"]),
          "postconditions": "{}".format(data["postconditions"]),
          "expectedResults": "{}".format(data["expectedResults"]),
          "actualResults": "{}".format(data["actualResults"]),
          "assignedTesters": "{}".format(data["assignedTesters"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return manual_test