def manual_test_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_manual_test",
        "description": "Generate a manual test node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate, is required to be 'TestStepNode'",
                    "enum": ["ManualTestCaseNode"]
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
                        "testData": {
                            "type": "string",
                            "description": ""
                        },
                        "assignedTesters": {
                            "type": "string",
                            "description": ""
                        }
                }, "required": ["title", "priority", "tags", "preconditions", "postconditions", "expectedResults", "actualResults", "testData", "assignedTesters"]},
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