def test_plan_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_test_plan",
        "description": "Generate a test plan node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate",
                    "enum": ["TestPlanNode"]
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
                        "numberOfAssignedTesters": {
                            "type": "number",
                            "description": ""
                        },
                        "dateOfExecution": {
                            "type": "string",
                            "description": ""
                        },
                        "estimation": {
                            "type": "string",
                            "description": ""
                        },
                        "riskAssessment": {
                            "type": "string",
                            "description": ""
                        },
                        "dataRequirements": {
                            "type": "string",
                            "description": ""
                        },
                        "overallExecutionResults": {
                            "type": "string",
                            "description": ""
                        }
                }, "required": ["title", "description", "numberOfAssignedTesters", "dateOfExecution", "estimation", "riskAssessment", "dataRequirements", "overallExecutionResults"]},
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