from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_manual_step_structure(node_id):
    true = True
    false = False
    manual_step = {
      "id": "{}".format(node_id),
      "position": {
        "x": 2400,
        "y": -int(node_id) * 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Manual Test Step",
        "version": 1,
        "name": "TestStepNode",
        "type": "TestStepNode",
        "baseClasses": [
          "TestStepNode"
        ],
        "category": "Manual Test",
        "description": "Single action a tester performs during manual testing (e.g., click a button, enter text).",
        "inputParams": [
          {
            "label": "Step ID",
            "name": "stepId",
            "type": "number",
            "description": "Unique identifier for the test step.",
            "id": "{}-input-stepId-number".format(node_id)
          },
          {
            "label": "Description",
            "name": "description",
            "type": "string",
            "rows": 4,
            "description": "Detailed instructions for the tester to follow.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-description-string".format(node_id)
          },
          {
            "label": "Required Input",
            "name": "requiredInput",
            "type": "string",
            "description": "Data or information the tester must provide to complete the test step.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-requiredInput-string".format(node_id)
          },
          {
            "label": "Expected Output",
            "name": "expectedOutput",
            "type": "string",
            "description": "Desired result or outcome of the test step.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-expectedOutput-string".format(node_id)
          }
        ],
        "inputAnchors": [
          {
            "label": "",
            "name": "input",
            "type": "ManualTestCaseNode",
            "optional": true,
            "id": "{}-input-input-ManualTestCaseNode".format(node_id)
          }
        ],
        "inputs": {
          "input": "{{ManualTestCaseNode_0.data.instance}}",
          "stepId": "",
          "description": "",
          "requiredInput": "",
          "expectedOutput": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-TestStepNode-TestStepNode".format(node_id),
            "name": "TestStepNode",
            "label": "TestStepNode",
            "description": "Single action a tester performs during manual testing (e.g., click a button, enter text).",
            "type": "TestStepNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 540,
      "selected": false,
      "positionAbsolute": {
        "x": 2400,
        "y": -int(node_id) * 450
      },
      "dragging": false
    }
    return manual_step

def reduced_manual_step(node_id, data, edge_list):
    manual_step = {
        "node": "TestStepNode",
        "node_id": "{}".format(node_id),
        "data": {
          "stepId": "{}".format(data["stepId"]),
          "description": "{}".format(data["description"]),
          "requiredInput": "{}".format(data["requiredInput"]),
          "expectedOutput": "{}".format(data["expectedOutput"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return manual_step