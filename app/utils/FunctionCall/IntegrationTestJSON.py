def integration_test_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_integration_test",
        "description": "Generate an integration test node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate, is required to be 'IntegrationTestNode'",
                    "enum": ["IntegrationTestNode"],
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
                        "priority": {
                            "type": "string",
                            "enum": ["High", "Medium", "Low"],
                            "description": ""
                        },
                        "tags": {
                            "type": "string",
                            "description": ""
                        },
                        "targetLayer": {
                            "type": "string",
                            "enum": ["Front-End", "Back-End"],
                            "description": ""
                        },
                }, "required": ["title", "description", "priority", "tags", "targetLayer"]},
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