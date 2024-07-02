from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_bdd_test_structure(node_id):
    true = True
    false = False
    bdd_test = {
      "id": "{}".format(node_id),
      "position": {
        "x": 2000,
        "y": 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "BDD Test Case",
        "version": 1,
        "name": "BDDTestCaseNode",
        "type": "BDDTestCaseNode",
        "baseClasses": [
          "BDDTestCaseNode"
        ],
        "category": "Test Case Nodes",
        "description": "User-focused test scenario written in plain language.",
        "inputParams": [
          {
            "label": "Title",
            "name": "title",
            "type": "string",
            "id": "{}-input-title-string".format(node_id)
          },
          {
            "label": "Background",
            "name": "background",
            "type": "string",
            "description": "Shared setup steps for BDD scenarios in a feature file.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-background-string".format(node_id)
          },
          {
            "label": "Scenario",
            "name": "scenario",
            "type": "string",
            "rows": 4,
            "description": "Specific user behavior example within a feature.",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-scenario-string".format(node_id)
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
            "label": "Gherkin Steps",
            "name": "gherkinSteps",
            "type": "datagrid",
            "description": "Structured actions in a BDD scenario using keywords like Given, When, Then.",
            "datagrid": [
              {
                "field": "Keyword",
                "headerName": "Keyword",
                "type": "singleSelect",
                "valueOptions": [
                  "Given",
                  "When",
                  "Then",
                  "And",
                  "But"
                ],
                "editable": true
              },
              {
                "field": "Text",
                "headerName": "Text",
                "type": "string",
                "editable": true,
                "flex": 1
              }
            ],
            "default": [
              {
                "Keyword": "Given",
                "Text": ""
              },
              {
                "Keyword": "When",
                "Text": ""
              },
              {
                "Keyword": "Then",
                "Text": ""
              }
            ],
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-gherkinSteps-datagrid".format(node_id)
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
          "title": "BDD",
          "background": "Background",
          "scenario": "Detailed scenario",
          "priority": "",
          "tags": "Stuff, stephen",
          "gherkinSteps": "[{\"Keyword\":\"Given\",\"Text\":\"The user is logged in\",\"id\":0},{\"Keyword\":\"When\",\"Text\":\"The page is loaded\",\"id\":1},{\"Keyword\":\"Then\",\"Text\":\"Something happens\",\"id\":2}]"
        },
        "outputAnchors": [
          {
            "id": "{}-output-BDDTestCaseNode-BDDTestCaseNode".format(node_id),
            "name": "BDDTestCaseNode",
            "label": "BDDTestCaseNode",
            "description": "User-focused test scenario written in plain language.",
            "type": "BDDTestCaseNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 558,
      "positionAbsolute": {
        "x": 2000,
        "y": 450
      },
      "selected": false,
      "dragging": false
    }
    return bdd_test


def modified_gherkins(data):
    # Data is a list, we need to convert it to a list of dictionaries
    data = eval(data)
    generated_gherkin = []
    for gherkin in data:
        generated_gherkin.append({
            "Keyword": "{}".format(gherkin['Keyword']),
            "Text": "{}".format(gherkin['Text'])
        })
    return generated_gherkin


def reduced_bdd_test(node_id, data, edge_list):
    bdd_test = {
        "node": "BDDTestCaseNode",
        "node_id": "{}".format(node_id),
        "data": {
          "title": "{}".format(data['title']),
          "background": "{}".format(data['background']),
          "scenario": "{}".format(data['scenario']),
          "priority": "{}".format(data['priority']),
          "tags": "",
          "gherkinSteps": "{}".format(modified_gherkins(data['gherkinSteps']))
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return bdd_test