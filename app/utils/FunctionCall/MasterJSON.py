def gen_master_workflow():
    return {
        "type": "function",
        "function": {
            "name": "gen_master_workflow",
            "description": "Generate a master workflow node that includes automated test, backend unit test, and backend integration test nodes",
            "parameters": {
                "type": "object",
                "properties": {
                    "automatedTestNode": {
                        "type": "object",
                        "properties": {
                            "node": {
                                "type": "string",
                                "enum": ["AutomatedTestCaseNode"]
                            },
                            "node_id": {
                                "type": "string"
                            },
                            "data": {
                                "type": "object",
                                "properties": {
                                    "title": { "type": "string" },
                                    "priority": { "type": "string", "enum": ["High", "Medium", "Low"] },
                                    "tags": { "type": "string" },
                                    "preconditions": { "type": "string" },
                                    "postconditions": { "type": "string" },
                                    "expectedResults": { "type": "string" },
                                    "actualResults": { "type": "string" },
                                    "scriptLocation": { "type": "string" },
                                    "programmingLanguage": { "type": "string" },
                                    "framework": { "type": "string" },
                                    "maintenanceEffort": { "type": "string", "enum": ["High", "Medium", "Low"] },
                                    "dependencies": { "type": "string" }
                                },
                                "required": ["title", "priority", "tags", "preconditions", "postconditions", "expectedResults", "actualResults", "scriptLocation", "programmingLanguage", "framework", "maintenanceEffort", "dependencies"]
                            },
                            "next_node": {
                                "type": "array",
                                "items": { "type": "string" }
                            }
                        },
                        "required": ["node", "node_id", "next_node"]
                    },
                    "backendUnitTestNode": {
                        "type": "object",
                        "properties": {
                            "node": {
                                "type": "string",
                                "enum": ["BackEndUnitTestNode"]
                            },
                            "node_id": {
                                "type": "string"
                            },
                            "data": {
                                "type": "object",
                                "properties": {
                                    "UnitTestClass": { "type": "string" },
                                    "Mocking": { "type": "string" }
                                },
                                "required": ["UnitTestClass", "Mocking"]
                            },
                            "next_node": {
                                "type": "array",
                                "items": { "type": "string" }
                            }
                        },
                        "required": ["node", "node_id", "next_node"]
                    },
                    "backendIntegrationTestNode": {
                        "type": "object",
                        "properties": {
                            "node": {
                                "type": "string",
                                "enum": ["BackEndIntegrationTestNode"]
                            },
                            "node_id": {
                                "type": "string"
                            },
                            "data": {
                                "type": "object",
                                "properties": {
                                    "IntegrationScope": { "type": "string" },
                                    "BackEndTechnology": { "type": "string" }
                                },
                                "required": ["IntegrationScope", "BackEndTechnology"]
                            },
                            "next_node": {
                                "type": "array",
                                "items": { "type": "string" }
                            }
                        },
                        "required": ["node", "node_id", "next_node"]
                    }
                },
            }
        }
    }