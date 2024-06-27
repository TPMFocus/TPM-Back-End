def test_suite_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_test_suite",
        "description": "Generate a test suite node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate, is required to be 'TestSuiteNode'",
                    "enum": ["TestSuiteNode"]
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
                        "exitCriteria": {
                            "type": "string",
                            "description": ""
                        }
                }, "required": ["title", "description", "exitCriteria"]},
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