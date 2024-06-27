from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_ui_interaction_structure(node_id):
    true = True
    false = False
    ui_interaction = {
      "id": "{}".format(node_id),
      "position": {
        "x": 2400,
        "y": 450
      },
      "type": "customNode",
      "data": {
        "id": "{}".format(node_id),
        "label": "UI Interaction",
        "version": 1,
        "name": "UIInteractionNode",
        "type": "UIInteractionNode",
        "baseClasses": [
          "UIInteractionNode"
        ],
        "category": "Automated Test",
        "description": "Action on a visual element and system's response.",
        "inputParams": [
          {
            "label": "Element",
            "name": "elementType",
            "type": "options",
            "options": [
              {
                "label": "Button",
                "name": "Button"
              },
              {
                "label": "Text field",
                "name": "Text field"
              },
              {
                "label": "Link",
                "name": "Link"
              },
              {
                "label": "Dropdown menu",
                "name": "Dropdown menu"
              },
              {
                "label": "Checkbox",
                "name": "Checkbox"
              },
              {
                "label": "Radio Buttons",
                "name": "Radio Buttons"
              },
              {
                "label": "Slider",
                "name": "Slider"
              },
              {
                "label": "Toggle Switches",
                "name": "Toggle Switches"
              },
              {
                "label": "Tab",
                "name": "Tab"
              },
              {
                "label": "Popup",
                "name": "Popup"
              },
              {
                "label": "Progress Bars",
                "name": "Progress Bars"
              }
            ],
            "additionalParams": true,
            "id": "{}-input-elementType-options".format(node_id)
          },
          {
            "label": "Identifier",
            "name": "identifier",
            "type": "string",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-identifier-string".format(node_id)
          },
          {
            "label": "Action",
            "name": "action",
            "type": "multiOptions",
            "options": [
              {
                "label": "Click",
                "name": "Click"
              },
              {
                "label": "Type",
                "name": "Type"
              },
              {
                "label": "Drag & Drop",
                "name": "Drag & Drop"
              },
              {
                "label": "Hover",
                "name": "Hover"
              },
              {
                "label": "Select",
                "name": "Select"
              },
              {
                "label": "Swipe",
                "name": "Swipe"
              },
              {
                "label": "Scroll",
                "name": "Scroll"
              },
              {
                "label": "Zoom",
                "name": "Zoom"
              }
            ],
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-action-multiOptions".format(node_id)
          },
          {
            "label": "Value",
            "name": "value",
            "type": "string",
            "description": "Value to be typed or selected (if appliable).",
            "optional": true,
            "additionalParams": true,
            "id": "{}-input-value-string".format(node_id)
          }
        ],
        "inputAnchors": [
          {
            "label": "Test Case",
            "name": "input",
            "type": "AutomatedTestCaseNode",
            "optional": true,
            "id": "{}-input-input-AutomatedTestCaseNode".format(node_id)
          },
          {
            "label": "UI Interaction",
            "name": "input",
            "type": "UIInteractionNode",
            "optional": true,
            "id": "{}-input-input-UIInteractionNode".format(node_id)
          }
        ],
        "inputs": {
          "input": "",
          "elementType": "",
          "identifier": "",
          "action": "",
          "value": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-UIInteractionNode-UIInteractionNode".format(node_id),
            "name": "UIInteractionNode",
            "label": "UIInteractionNode",
            "description": "Action on a visual element and system's response.",
            "type": "UIInteractionNode"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 265,
      "selected": false,
      "positionAbsolute": {
        "x": 2400,
        "y": 450
      },
      "dragging": false
    }
    return ui_interaction

def reduced_ui_interaction_structure(node_id, data, edge_list):
    ui_interaction = {
        "node": "UIInteractionNode",
        "node_id": "{}".format(node_id),
        "data": {
          "elementType": "{}".format(data["elementType"]),
          "identifier": "{}".format(data["identifier"]),
          "action": "{}".format(data["action"]),
          "value": "{}".format(data["value"]),
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return ui_interaction