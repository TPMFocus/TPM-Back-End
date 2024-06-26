def integration_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_integration",
        "description": "Generate an integration node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "",
                    "enum": ["IntegrationNode"]
                },
                "node_id": {
                    "type": "string",
                    "description": ""
                },
                "data": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "JIRA_URL": {
                            "type": "string",
                            "description": ""
                        },
                        "projectkey": {
                            "type": "string",
                            "description": ""
                        },
                        "authentication": {
                            "type": "string",
                            "description": ""
                        }
                }, "required": ["JIRA_URL", "projectkey", "authentication"]},
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