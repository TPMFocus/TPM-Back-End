def ui_interactions_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_ui_interactions",
        "description": "Generate a UI interactions node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate",
                    "enum": ["UIInteractionNode"]
                },
                "node_id": {
                    "type": "string",
                    "description": ""
                },
                "data": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "element": {
                            "type": "string",
                            "enum": ["Button", "Text field", "Link", "Dropdown menu", "Checkbox", "Radio Buttons", "Slider", "Toggle Switches", "Tab", "Popup", "Progress Bars"],
                            "description": ""
                        },
                        "identifier": {
                            "type": "string",
                            "description": ""
                        },
                        "action": {
                            "type": "string",
                            "enum": ["Click", "Type", "Drag & Drop", "Hover", "Select", "Swipe", "Scroll", "Zoom"],
                            "description": ""
                        }
                }, "required": ["element", "identifier", "action"]},
                "next_node": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": ""
                },
            },
            "required": ["node", "node_id", "next_node"]
        }
    }
}