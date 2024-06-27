def note_json():
    return {
    "type": "function",
    "function": {
        "name": "gen_note",
        "description": "Generate a note node",
        "parameters": {
            "type": "object",
            "properties": {
                "node": {
                    "type": "string",
                    "description": "The type of node to generate, is required to be 'stickyNote'",
                    "enum": ["stickyNote"]
                },
                "node_id": {
                    "type": "string",
                    "description": ""
                },
                "data": {
                    "type": "object",
                    "description": "",
                    "properties": {
                        "note": {
                            "type": "string",
                            "description": ""
                        }
                }, "required": ["note"]},
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