from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_test_phase_structure(node_id):
    true = True
    false = False
    test_phase = {
      "id": "{}".format(node_id),
      "position": {
        "x": 400,
        "y": -int(node_id) * 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Test Phase",
        "version": 1,
        "name": "TestingPhaseNode",
        "type": "TestingPhaseNode",
        "baseClasses": [
          "TestingPhaseNode"
        ],
        "category": "Main Nodes",
        "description": "Dedicated stage in software development focused on identifying and fixing bugs before launch.",
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
            "label": "Start Date",
            "name": "startDate",
            "type": "date",
            "description": "Start date of the test phase.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-startDate-date".format(node_id)
          },
          {
            "label": "End Date",
            "name": "endDate",
            "type": "date",
            "description": "End date of the test phase.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-endDate-date".format(node_id)
          },
          {
            "label": "Estimation",
            "name": "estimation",
            "type": "string",
            "description": "Estimation of the test phase.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-estimation-string".format(node_id)
          }
        ],
        "inputAnchors": [
          {
            "label": "",
            "name": "input",
            "type": "TestStrategyNode",
            "optional": true,
            "id": "{}-input-input-TestStrategyNode".format(node_id)
          }
        ],
        "inputs": {
          "input": "{{testStrategyNode_0.data.instance}}",
          "title": "Test Phase v1",
          "description": "Example of a test phase",
          "startDate": "",
          "endDate": "",
          "estimation": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-TestingPhaseNode-TestingPhaseNode".format(node_id),
            "name": "TestingPhaseNode",
            "label": "TestingPhaseNode",
            "description": "Dedicated stage in software development focused on identifying and fixing bugs before launch.",
            "type": "TestingPhaseNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 540,
      "selected": false,
      "positionAbsolute": {
        "x": 400,
        "y": -int(node_id) * 450
      },
      "dragging": false
    }
    return test_phase


def reduced_test_phase(node_id, data, edge_list):
    test_phase = {
        "node": "TestingPhaseNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data["title"]),
          "description": "{}".format(data["description"]),
          "startDate": "{}".format(data["startDate"]),
          "endDate": "{}".format(data["endDate"]),
          "estimation": "{}".format(data["estimation"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return test_phase