from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_test_plan_structure(node_id):
    true = True
    false = False
    test_plan = {
      "id": "{}".format(node_id),
      "position": {
        "x": 800,
        "y": 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Test Plan",
        "version": 1,
        "name": "TestPlanNode",
        "type": "TestPlanNode",
        "baseClasses": [
          "TestPlanNode"
        ],
        "category": "Main Nodes",
        "description": "A formal document outlining the strategy, scope, resources, and schedule for testing a software application or system.",
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
            "label": "Number of Assigned Testers",
            "name": "numberOfAssignedTesters",
            "type": "number",
            "step": 1,
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-numberOfAssignedTesters-number".format(node_id)
          },
          {
            "label": "Date of execution",
            "name": "dateOfExecution",
            "type": "string",
            "description": "Date of execution of the test phase.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-dateOfExecution-string".format(node_id)
          },
          {
            "label": "Estimation",
            "name": "estimation",
            "type": "string",
            "description": "Estimation of the test plan.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-estimation-string".format(node_id)
          },
          {
            "label": "Risk Assessment",
            "name": "riskAssessment",
            "type": "string",
            "rows": 4,
            "description": "Risk assessment of the test plan.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-riskAssessment-string".format(node_id)
          },
          {
            "label": "Data Requirements",
            "name": "dataRequirements",
            "type": "string",
            "rows": 4,
            "description": "Data requirements of the test plan.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-dataRequirements-string".format(node_id)
          },
          {
            "label": "Overall Execution Results",
            "name": "overallExecutionResults",
            "type": "string",
            "rows": 2,
            "description": "Overall execution results of the test plan.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-overallExecutionResults-string".format(node_id)
          }
        ],
        "inputAnchors": [
          {
            "label": "",
            "name": "input",
            "type": "TestingPhaseNode",
            "optional": true,
            "id": "{}-input-input-TestingPhaseNode".format(node_id)
          },
          {
            "label": "Environment",
            "name": "inputEnvironment",
            "type": "TestEnvironmentNode",
            "optional": true,
            "id": "{}-input-inputEnvironment-TestEnvironmentNode".format(node_id)
          }
        ],
        "inputs": {
          "input": "{{TestingPhaseNode_0.data.instance}}",
          "inputEnvironment": "{{TestEnvironmentNode_0.data.instance}}",
          "title": "",
          "description": "",
          "numberOfAssignedTesters": "",
          "dateOfExecution": "",
          "estimation": "",
          "riskAssessment": "",
          "dataRequirements": "",
          "overallExecutionResults": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-TestPlanNode-TestPlanNode".format(node_id),
            "name": "TestPlanNode",
            "label": "TestPlanNode",
            "description": "A formal document outlining the strategy, scope, resources, and schedule for testing a software application or system.",
            "type": "TestPlanNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 591,
      "selected": false,
      "positionAbsolute": {
        "x": 800,
        "y": 450
      },
      "dragging": false
    }
    return test_plan


def reduced_test_plan(node_id, data, edge_list):
    test_plan = {
        "node": "TestPlanNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data["title"]),
          "description": "{}".format(data["description"]),
          "numberOfAssignedTesters": "{}".format(data["numberOfAssignedTesters"]),
          "dateOfExecution": "{}".format(data["dateOfExecution"]),
          "estimation": "{}".format(data["estimation"]),
          "riskAssessment": "{}".format(data["riskAssessment"]),
          "dataRequirements": "{}".format(data["dataRequirements"]),
          "overallExecutionResults": "{}".format(data["overallExecutionResults"])
        },
        "next_node": get_next_node_id(node_id, edge_list),
    }
    return test_plan