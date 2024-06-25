from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_code_quality_checks_structure(node_id):
    true = True
    false = False
    code_quality_checks = {
      "id": "{}".format(node_id),
      "position": {
        "x": 1600,
        "y": -int(node_id) * 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "Code Quality Checks",
        "version": 1,
        "name": "CodeQualityChecksNode",
        "type": "CodeQualityChecksNode",
        "baseClasses": [
          "CodeQualityChecksNode"
        ],
        "category": "Test Case Nodes",
        "description": "Automated or manual reviews to ensure code meets coding standards and best practices.",
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
            "label": "Description",
            "name": "description",
            "type": "string",
            "rows": 4,
            "optional": true,
            "id": "{}-input-description-string".format(node_id)
          },
          {
            "label": "Tags",
            "name": "tags",
            "type": "string",
            "optional": true,
            "id": "{}-input-tags-string".format(node_id)
          },
          {
            "label": "Checks",
            "name": "checks",
            "type": "datagrid",
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
                "Metric": "Code Coverage",
                "Value": 0
              },
              {
                "Metric": "Static Code Analysis",
                "Value": 0
              },
              {
                "Metric": "Resource Utilization",
                "Value": 0
              }
            ],
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-checks-datagrid".format(node_id)
          },
          {
            "label": "Tools",
            "name": "tools",
            "type": "string",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-tools-string".format(node_id)
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
          "priority": "",
          "description": "",
          "tags": "",
          "checks": [
            {
              "Metric": "Code Coverage",
              "Value": 0
            },
            {
              "Metric": "Static Code Analysis",
              "Value": 0
            },
            {
              "Metric": "Resource Utilization",
              "Value": 0
            }
          ],
          "tools": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-CodeQualityChecksNode-CodeQualityChecksNode".format(node_id),
            "name": "CodeQualityChecksNode",
            "label": "CodeQualityChecksNode",
            "description": "Automated or manual reviews to ensure code meets coding standards and best practices.",
            "type": "CodeQualityChecksNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 735,
      "positionAbsolute": {
        "x": 1600,
        "y": -int(node_id) * 450
      },
      "selected": false,
      "dragging": false
    }
    return code_quality_checks


def modified_checks(data):
    data = eval(data)
    generated_checks = []
    for check in data:
        generated_checks.append({
            "Metric": "{}".format(check["Metric"]),
            "Value": "{}".format(check["Value"])
        })
    return generated_checks


def reduced_code_quality_checks(node_id, data, edge_list):
    code_quality_checks = {
        "node": "CodeQualityChecksNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data["title"]),
          "priority": "{}".format(data["priority"]),
          "description": "{}".format(data["description"]),
          "tags": "{}".format(data["tags"]),
          "checks": "{}".format(modified_checks(data["checks"])),
          "tools": "{}".format(data["tools"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return code_quality_checks