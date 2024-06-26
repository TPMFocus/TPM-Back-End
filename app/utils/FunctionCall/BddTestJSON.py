def bdd_test_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_bdd_test",
        "description": "Generate a BDD test node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "",
                    "enum": ["BDDTestCaseNode"],
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
                        "background": {
                            "type": "string",
                            "description": ""
                        },
                        "scenario": {
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
                        "gherkinSteps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "Keyword": {
                                        "type": "string",
                                        "enum": ["Given", "When", "Then", "And", "But"],
                                        "description": ""
                                    },
                                    "Text": {
                                        "type": "string",
                                        "description": ""
                                    }
                                },
                            },
                            "description": ""
                        },
                    },
                    "required": ["title", "background", "scenario", "priority", "tags", "gherkinSteps"]
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