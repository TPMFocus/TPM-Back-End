from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_performance_test_structure(node_id):
    true = True
    false = False
    performance_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 1600,
        "y": 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Performace Test Case",
        "version": 1,
        "name": "PerformanceTestNode",
        "type": "PerformanceTestNode",
        "baseClasses": [
          "PerformanceTestNode"
        ],
        "category": "Test Case Nodes",
        "description": "Evaluation of software's responsiveness, stability, and scalability under a specific load.",
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
            "label": "Metrics",
            "name": "metrics",
            "type": "datagrid",
            "description": "Metrics to be measured for the performance test.",
            "datagrid": [
              {
                "field": "Metric",
                "label": "Metric",
                "type": "string",
                "flex": 1,
                "editable": true
              },
              {
                "field": "Value",
                "label": "Value",
                "type": "number",
                "editable": true
              }
            ],
            "default": [
              {
                "Metric": "Response Time",
                "Value": 0
              },
              {
                "Metric": "Throughput",
                "Value": 0
              },
              {
                "Metric": "Resource Utilization",
                "Value": 0
              }
            ],
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-metrics-datagrid".format(node_id)
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
          "description": "",
          "priority": "",
          "tags": "",
          "metrics": "[{\"Metric\":\"Response Time\",\"Value\":10,\"id\":0},{\"Metric\":\"Throughput\",\"Value\":20,\"id\":1},{\"Metric\":\"Resource Utilization\",\"Value\":10.1,\"id\":2}]"
        },
        "outputAnchors": [
          {
            "id": "{}-output-PerformanceTestNode-PerformanceTestNode".format(node_id),
            "name": "PerformanceTestNode",
            "label": "PerformanceTestNode",
            "description": "Evaluation of software's responsiveness, stability, and scalability under a specific load.",
            "type": "PerformanceTestNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 735,
      "selected": false,
      "positionAbsolute": {
        "x": 1600,
        "y": 450
      },
      "dragging": false
    }
    return performance_test

def modified_metrics(data):
    metrics = []
    for metric in data:
        metrics.append({
            "Metric": "{}".format(metric["Metric"]),
            "Value": "{}".format(metric["Value"])
        })
    return metrics


def reduced_performance_test(node_id, data, edge_list):
    performance_test = {
        "node": "PerformanceTestNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data["title"]),
          "description": "{}".format(data["description"]),
          "priority": "{}".format(data["priority"]),
          "tags": "{}".format(data["tags"]),
          "metrics": "{}".format(modified_metrics(data["metrics"]))
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return performance_test