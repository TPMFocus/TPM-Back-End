def performance_test_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_performance_test",
        "description": "Generate a performance test node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate, is required to be 'PerformanceTestNode'",
                    "enum": ["PerformanceTestNode"]
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
                            "enum": ["High", "Medium", "Low"],
                            "description": ""
                        },
                        "tags": {
                            "type": "string",
                            "description": ""
                        },
                        "metrics": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "Metric": {
                                        "type": "string",
                                        "description": ""
                                    },
                                    "Value": {
                                        "type": "number",
                                        "description": ""
                                    }
                                },
                            },
                            "description": ""
                        },
                }, "required": ["title", "description", "priority", "tags", "metrics"]},
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