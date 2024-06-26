def security_test_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_security_test",
        "description": "Generate a security test node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "",
                    "enum": ["SecurityTestNode"]
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
                            "type": "number",
                            "enum": ["High", "Medium", "Low"],
                            "description": ""
                        },
                        "tags": {
                            "type": "string",
                            "description": ""
                        },
                        "type": {
                            "type": "string",
                            "enum": ["Penetration Testing", "Vulnerability Scanning", "Other"],
                            "description": ""
                        }
                }, "required": ["title", "description", "priority", "tags", "type"]},
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