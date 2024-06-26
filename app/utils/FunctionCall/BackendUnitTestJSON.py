def backend_unit_test_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_backend_unit_test",
        "description": "Generate a backend unit test node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "",
                    "enum": ["BackEndUnitTestNode"],
                },
                "node_id": {
                    "type": "string",
                    "description": ""
                },
                "data": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "UnitTestClass": {
                            "type": "string",
                            "description": ""
                        },
                        "Mocking": {
                            "type": "string",
                            "description": ""
                        }
                    },
                    "required": ["UnitTestClass", "Mocking"]
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