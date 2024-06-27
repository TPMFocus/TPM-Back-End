from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_execution_details_structure(node_id):
    true = True
    false = False
    execution_details = {
      "id": "{}".format(node_id),
      "position": {
        "x": 1200,
        "y": 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Execution Details",
        "version": 1,
        "name": "ExecutionDetailsNode",
        "type": "ExecutionDetailsNode",
        "baseClasses": [
          "ExecutionDetailsNode"
        ],
        "category": "Main Nodes",
        "description": "Execution History (Date, Estimate, Actual Time, Status)",
        "inputParams": [
          {
            "label": "Date of Execution",
            "name": "dateOfExecution",
            "type": "string",
            "description": "The date at which the test was executed.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-dateOfExecution-string".format(node_id)
          },
          {
            "label": "Estimation",
            "name": "estimation",
            "type": "string",
            "description": "The estimated time for the test to be executed.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-estimation-string".format(node_id)
          },
          {
            "label": "Real Execution Time",
            "name": "realExecutionTime",
            "type": "string",
            "description": "The actual time taken to execute the test.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-realExecutionTime-string".format(node_id)
          },
          {
            "label": "Execution Status",
            "name": "passFailStatus",
            "type": "options",
            "options": [
              {
                "label": "Pass",
                "name": "Pass"
              },
              {
                "label": "Fail",
                "name": "Fail"
              }
            ],
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-passFailStatus-options".format(node_id)
          }
        ],
        "inputAnchors": [],
        "inputs": {
          "dateOfExecution": "",
          "estimation": "",
          "realExecutionTime": "",
          "passFailStatus": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-ExecutionDetailsNode-ExecutionDetailsNode".format(node_id),
            "name": "ExecutionDetailsNode",
            "label": "ExecutionDetailsNode",
            "description": "Execution History (Date, Estimate, Actual Time, Status)",
            "type": "ExecutionDetailsNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 253,
      "selected": false,
      "positionAbsolute": {
        "x": 1200,
        "y": 450
      },
      "dragging": false
    }
    return execution_details


def reduced_execution_details(node_id, data, edge_list):
    execution_details = {
        "node": "ExecutionDetailsNode",
        "node_id": "{}".format(node_id),
        "data": {
          "dateOfExecution": "{}".format(data["dateOfExecution"]),
          "estimation": "{}".format(data["estimation"]),
          "realExecutionTime": "{}".format(data["realExecutionTime"]),
          "passFailStatus": "{}".format(data["passFailStatus"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return execution_details