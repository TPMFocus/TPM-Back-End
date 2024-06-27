def thrid_party_checks_test_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_third_party_checks_test",
        "description": "Generate a third party checks test node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate, is required to be 'ThirdPartyChecksNode'",
                    "enum": ["ThirdPartyChecksNode"]
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
                            "enum": ["Low", "Medium", "High"],
                            "description": ""
                        },
                        "tags": {
                            "type": "string",
                            "description": ""
                        },
                        "type": {
                            "type": "string",
                            "description": ""
                        },
                        "tools": {
                            "type": "string",
                            "description": ""
                        }
                }, "required": ["title", "description", "priority", "tags", "type", "tools"]},
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