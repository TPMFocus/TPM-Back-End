def frontend_integration_test_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_frontend_integration_test",
        "description": "Generate a frontend integration test node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate",
                    "enum": ["FrontEndIntegrationTestNode"]
                },
                "node_id": {
                    "type": "string",
                    "description": ""
                },
                "data": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "IntegrationScope": {
                            "type": "string",
                            "description": ""
                        },
                        "FrontEndTechnology": {
                            "type": "string",
                            "description": ""
                        }
                },
                "required": ["IntegrationScope", "FrontEndTechnology"]},
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