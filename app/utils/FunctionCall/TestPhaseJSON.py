def test_phase_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_test_phase",
        "description": "Generate a test phase node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate",
                    "enum": ["TestingPhaseNode"]
                },
                "node_id": {
                    "type": "string",
                    "description": ""
                },
                "data": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": ""
                        },
                        "description": {
                            "type": "string",
                            "description": ""
                        },
                        "startDate": {
                            "type": "string",
                            "description": ""
                        },
                        "endDate": {
                            "type": "string",
                            "description": ""
                        },
                        "estimation": {
                            "type": "string",
                            "description": ""
                        }
                }, "required": ["title", "description", "startDate", "endDate", "estimation"]},
                "next_node": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Followed by a test plan node if it exists, otherwise nothing."
                },
            },
            "required": ["node", "node_id", "next_node"]
        }
    }
}