def backend_integration_test_json():
    json_response = {
        "type": "function",
        "function": {
            "name": "gen_backend_integration_test",
            "description": "Generate a backend integration test node",
            "parameters": {
                "type": "object",
                "properties": {
                    "node": {
                        "type": "string",
                        "description": "",
                        "enum": ["BackEndIntegrationTestNode"]
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
                            "BackEndTechnology": {
                                "type": "string",
                                "description": ""
                            }
                    },
                    "required": ["IntegrationScope", "BackEndTechnology"]
                    },
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
    return json_response