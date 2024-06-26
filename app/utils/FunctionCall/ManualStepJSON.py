def manual_step_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_manual_step",
        "description": "Generate a manual step node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate",
                    "enum": ["TestStepNode"],
                },
                "node_id": {
                    "type": "string",
                    "description": ""
                },
                "data": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "stepId": {
                            "type": "number",
                            "description": ""
                        },
                        "description": {
                            "type": "string",
                            "description": ""
                        },
                        "requiredInput": {
                            "type": "string",
                            "description": ""
                        },
                        "expectedOutput": {
                            "type": "string",
                            "description": ""
                        }
                }, "required": ["stepId", "description", "requiredInput", "expectedOutput"]},
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