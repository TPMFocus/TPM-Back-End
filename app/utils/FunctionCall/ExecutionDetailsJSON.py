def execution_details_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_execution_details",
        "description": "Generate execution details node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate, is required to be 'ExecutionDetailsNode'",
                    "enum": ["ExecutionDetailsNode"]
                },
                "node_id": {
                    "type": "string",
                    "description": ""
                },
                "data": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "dateOfExecution": {
                            "type": "string",
                            "description": ""
                        },
                        "estimation": {
                            "type": "string",
                            "description": ""
                        },
                        "realExecutionTime": {
                            "type": "string",
                            "description": ""
                        },
                        "passFailStatus": {
                            "type": "string",
                            "enum": ["Pass", "Fail"],
                            "description": ""
                        }
                },
                "required": ["dateOfExecution", "estimation", "realExecutionTime", "passFailStatus"]},
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