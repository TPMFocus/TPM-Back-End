from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_test_strategy_structure(node_id):
    true = True
    false = False
    test_strategy = {
      "id": "{}".format(node_id),
      "position": {
        "x": 0,
        "y": -int(node_id) * 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Test Strategy",
        "version": 1,
        "name": "testStrategyNode",
        "type": "TestStrategyNode",
        "baseClasses": [
          "TestStrategyNode"
        ],
        "category": "Main Nodes",
        "description": "High-level plan outlining the overall testing approach for a project.",
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
            "label": "Data Considerations",
            "name": "dataConsiderations",
            "type": "string",
            "rows": 4,
            "description": "Overview of the test plan, detailing scope, resources, schedule, and testing phases.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-dataConsiderations-string".format(node_id)
          }
        ],
        "inputAnchors": [],
        "inputs": {
          "title": "Test Strategy",
          "description": "This is an example of a test strategy",
          "dataConsiderations": "This is an example of Data Considerations"
        },
        "outputAnchors": [
          {
            "id": "{}-output-testStrategyNode-TestStrategyNode".format(node_id),
            "name": "testStrategyNode",
            "label": "TestStrategyNode",
            "description": "High-level plan outlining the overall testing approach for a project.",
            "type": "TestStrategyNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 508,
      "selected": false,
      "positionAbsolute": {
        "x": 0,
        "y": -int(node_id) * 450
      },
      "dragging": false
    }
    return test_strategy

def reduced_test_strategy(node_id, data, edge_list):
    test_strategy = {
        "node": "TestStrategyNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data['title']),
          "description": "{}".format(data['description']),
          "dataConsiderations": "{}".format(data['dataConsiderations'])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return test_strategy