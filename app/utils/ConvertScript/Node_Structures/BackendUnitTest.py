from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_backend_unit_test_structure(node_id):
    true = True
    false = False
    backend_unit_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 2400,
        "y": -int(node_id) * 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Back End Unit Test Case",
        "version": 1,
        "name": "BackEndUnitTestNode",
        "type": "BackEndUnitTestNode",
        "baseClasses": [
          "BackEndUnitTestNode"
        ],
        "category": "Unit Test Nodes",
        "description": "Focused scripts that automatically validate individual backend components in isolation.",
        "inputParams": [
          {
            "label": "Unit Test Class",
            "name": "UnitTestClass",
            "type": "string",
            "additionalParams": true,
            "id": "{}-input-UnitTestClass-string".format(node_id)
          },
          {
            "label": "Mocking Framework",
            "name": "Mocking",
            "type": "string",
            "description": "(e.g., Mockito, Mock, PowerMock)",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-Mocking-string".format(node_id)
          }
        ],
        "inputAnchors": [
          {
            "label": "",
            "name": "input",
            "type": "UnitTestNode",
            "id": "{}-input-input-UnitTestNode".format(node_id)
          }
        ],
        "inputs": {
          "input": "{{UnitTestNode_0.data.instance}}",
          "UnitTestClass": "",
          "Mocking": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-BackEndUnitTestNode-BackEndUnitTestNode".format(node_id),
            "name": "BackEndUnitTestNode",
            "label": "BackEndUnitTestNode",
            "description": "Focused scripts that automatically validate individual backend components in isolation.",
            "type": "BackEndUnitTestNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 283,
      "selected": false,
      "positionAbsolute": {
        "x": 2400,
        "y": -int(node_id) * 450
      },
      "dragging": false
    }
    return backend_unit_test

def reduced_backend_unit_test(node_id, data, edge_list):
    backend_unit_test = {
        "node": "BackEndUnitTestNode",
        "node_id": "{}".format(node_id),
        "data": {
          "UnitTestClass": "{}".format(data["UnitTestClass"]),
          "Mocking": "{}".format(data["Mocking"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return backend_unit_test