def code_quality_checks_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_code_quality_checks",
        "description": "Generate a code quality checks node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate, is required to be 'CodeQualityChecksNode'",
                    "enum": ["CodeQualityChecksNode"]
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
                        "description": {
                            "type": "string",
                            "description": ""
                        },
                        "tags": {
                            "type": "string",
                            "description": ""
                        },
                        "checks": {
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
                },
                    "required": ["title", "priority", "description", "tags", "checks"]
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