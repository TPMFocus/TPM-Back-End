def test_environment_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_test_environment",
        "description": "Generate a test environment node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "",
                    "enum": ["TestEnvironmentNode"]
                },
                "node_id": {
                    "type": "string",
                    "description": ""
                },
                "data": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": ""
                        },
                        "url": {
                            "type": "string",
                            "description": ""
                        },
                        "database": {
                            "type": "string",
                            "description": ""
                        },
                        "credentials": {
                            "type": "string",
                            "description": ""
                        },
                        "tools": {
                            "type": "string",
                            "description": ""
                        }
                }, "required": ["name", "url", "database", "credentials", "tools"]},
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