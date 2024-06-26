def frontend_unit_test_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_frontend_unit_test",
        "description": "Generate a frontend unit test node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate",
                    "enum": ["FrontEndUnitTestNode"]
                },
                "node_id": {
                    "type": "string",
                    "description": ""
                },
                "data": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "UITestFramework": {
                            "type": "string",
                            "description": ""
                        },
                        "UIElements": {
                            "type": "string",
                            "description": ""
                        }
                }, 
                "required": ["UITestFramework", "UIElements"]},
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