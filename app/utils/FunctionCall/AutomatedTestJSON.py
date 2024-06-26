def automated_test_json():
    json_response = {
        "type": "function",
        "function": {
            "name": "gen_automated_test",
            "description": "Generate an automated test node",
            "parameters": {
                "type": "object",
                "properties": {
                    "node": {
                        "type": "string",
                        "description": "",
                        "enum": ["AutomatedTestCaseNode"]
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
                            "priority": {
                                "type": "string",
                                "enum": ["High", "Medium", "Low"],
                                "description": ""
                            },
                            "tags": {
                                "type": "string",
                                "description": ""
                            },
                            "preconditions": {
                                "type": "string",
                                "description": ""
                            },
                            "postconditions": {
                                "type": "string",
                                "description": ""
                            },
                            "expectedResults": {
                                "type": "string",
                                "description": ""
                            },
                            "actualResults": {
                                "type": "string",
                                "description": ""
                            },
                            "scriptLocation": {
                                "type": "string",
                                "description": ""
                            },
                            "programmingLanguage": {
                                "type": "string",
                                "description": ""
                            },
                            "framework": {
                                "type": "string",
                                "description": ""
                            },
                            "maintenanceEffort": {
                                "type": "string",
                                "enum": ["High", "Medium", "Low"],
                                "description": ""
                            },
                            "dependencies": {
                                "type": "string",
                                "description": ""
                            }
                        },
                        "required": ["title", "priority", "tags", "preconditions", "postconditions", "expectedResults", "actualResults", "scriptLocation", "programmingLanguage", "framework", "maintenanceEffort", "dependencies"]
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
