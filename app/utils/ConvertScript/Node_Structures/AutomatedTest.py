from app.utils.ConvertScript.GetNextNode import get_next_node_id, extract_int

def generate_automated_test_structure(node_id):
    true = True
    false = False
    automated_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 2000,
        "y": extract_int(node_id) * 600
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Automated Test Case",
        "version": 1,
        "name": "AutomatedTestCaseNode",
        "type": "AutomatedTestCaseNode",
        "baseClasses": [
          "AutomatedTestCaseNode"
        ],
        "category": "Automated Test",
        "description": "Script or code that executes test steps and verifies software functionality without human intervention.",
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
            "description": "",
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
            "label": "Script Location",
            "name": "scriptLocation",
            "type": "string",
            "description": "Path to the test script file.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-scriptLocation-string".format(node_id)
          },
          {
            "label": "Programming Language",
            "name": "programmingLanguage",
            "type": "string",
            "description": "Programming language used to write the test script.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-programmingLanguage-string".format(node_id)
          },
          {
            "label": "Framework",
            "name": "framework",
            "type": "string",
            "description": "Testing framework used to execute the test script.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-framework-string".format(node_id)
          },
          {
            "label": "Maintenance Effort",
            "name": "maintenanceEffort",
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
            "additionalParams": true,
            "id": "{}-input-maintenanceEffort-options".format(node_id)
          },
          {
            "label": "Dependencies",
            "name": "dependencies",
            "type": "string",
            "rows": 2,
            "description": "List of dependencies for the automated test case.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-dependencies-string".format(node_id)
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
          "priority": "High",
          "tags": "",
          "preconditions": "",
          "postconditions": "",
          "expectedResults": "",
          "actualResults": "",
          "scriptLocation": "",
          "programmingLanguage": "",
          "framework": "",
          "maintenanceEffort": "",
          "dependencies": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-AutomatedTestCaseNode-AutomatedTestCaseNode".format(node_id),
            "name": "AutomatedTestCaseNode",
            "label": "AutomatedTestCaseNode",
            "description": "Script or code that executes test steps and verifies software functionality without human intervention.",
            "type": "AutomatedTestCaseNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 558,
      "positionAbsolute": {
        "x": 2000,
        "y": extract_int(node_id) * 600
      },
      "selected": false,
      "dragging": false
    }
    return automated_test

    

def reduced_automated_test(node_id, data, edge_list):
    automated_test = {
        "node": "AutomatedTestCaseNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data["title"]),
          "priority": "{}".format(data["priority"]),
          "tags": "{}".format(data["tags"]),
          "preconditions": "{}".format(data["preconditions"]),
          "postconditions": "{}".format(data["postconditions"]),
          "expectedResults": "{}".format(data["expectedResults"]),
          "actualResults": "{}".format(data["actualResults"]),
          "scriptLocation": "{}".format(data["scriptLocation"]),
          "programmingLanguage": "{}".format(data["programmingLanguage"]),
          "framework": "{}".format(data["framework"]),
          "maintenanceEffort": "{}".format(data["maintenanceEffort"]),
          "dependencies": "{}".format(data["dependencies"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return automated_test