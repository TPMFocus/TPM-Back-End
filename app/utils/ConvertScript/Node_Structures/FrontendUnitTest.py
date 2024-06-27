from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_frontend_unit_test_structure(node_id):
    true = True
    false = False
    frontend_unit_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 2400,
        "y": 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Front End Unit Test Case",
        "version": 1,
        "name": "FrontEndUnitTestNode",
        "type": "FrontEndUnitTestNode",
        "baseClasses": [
          "FrontEndUnitTestNode"
        ],
        "category": "Unit Test Nodes",
        "description": "Isolated test of a single frontend component's functionality.",
        "inputParams": [
          {
            "label": "UI Test Framework",
            "name": "UITestFramework",
            "type": "string",
            "description": "The UI test framework used to run the test.",
            "additionalParams": true,
            "id": "{}-input-UITestFramework-string".format(node_id)
          },
          {
            "label": "UI Elements",
            "name": "UIElements",
            "type": "string",
            "description": "The UI elements that are being tested.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-UIElements-string".format(node_id)
          }
        ],
        "inputAnchors": [
          {
            "label": "",
            "name": "input",
            "type": "UnitTestNode",
            "optional": true,
            "id": "{}-input-input-UnitTestNode".format(node_id)
          }
        ],
        "inputs": {
          "input": "{{UnitTestNode_0.data.instance}}",
          "UITestFramework": "",
          "UIElements": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-FrontEndUnitTestNode-FrontEndUnitTestNode".format(node_id),
            "name": "FrontEndUnitTestNode",
            "label": "FrontEndUnitTestNode",
            "description": "Isolated test of a single frontend component's functionality.",
            "type": "FrontEndUnitTestNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 410,
      "positionAbsolute": {
        "x": 2400,
        "y": 450
      },
      "selected": false
    }
    return frontend_unit_test

def reduced_frontend_unit_test(node_id, data):
    frontend_unit_test = {
        "node": "FrontEndUnitTestNode",
        "node_id": "{}".format(node_id),
        "data": {
          "UITestFramework": "{}".format(data["UITestFramework"]),
          "UIElements": "{}".format(data["UIElements"])
        }
    }
    return frontend_unit_test