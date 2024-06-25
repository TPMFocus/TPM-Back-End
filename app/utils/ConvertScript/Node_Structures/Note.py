from app.utils.ConvertScript.GetNextNode import get_next_node_id

def generate_note_structure(node_id):
    true = True
    false = False
    note = {
      "id": "{}".format(node_id),
      "position": {
        "x": -400,
        "y": -int(node_id) * 450
      },
      "type": "stickyNote",
      "data": {
        "id": "{}".format(node_id),
        "label": "Note",
        "version": 1,
        "name": "NoteNode",
        "type": "StickyNote",
        "baseClasses": [
          "StickyNote"
        ],
        "category": "Main Nodes",
        "description": "Add a sticky note",
        "inputParams": [
          {
            "label": "",
            "name": "note",
            "type": "string",
            "rows": 1,
            "placeholder": "Type something here",
            "optional": true,
            "id": "{}-input-note-string".format(node_id)
          }
        ],
        "inputAnchors": [],
        "inputs": {
          "note": ""
        },
        "outputAnchors": [
          {
            "id": "{}-output-NoteNode-StickyNote".format(node_id),
            "name": "NoteNode",
            "label": "StickyNote",
            "description": "Add a sticky note",
            "type": "StickyNote"
          }
        ],
        "outputs": {},
        "selected": false
      },
      "width": 300,
      "height": 42,
      "positionAbsolute": {
        "x": -400,
        "y": -int(node_id) * 450
      },
      "selected": false,
      "dragging": false
    }
    return note

def reduced_note(node_id, data, edge_list):
    note = {
        "node": "StickyNote",
        "node_id": "{}".format(node_id),
        "data": {
          "note": "{}".format(data["note"])
        },
        "next_node": get_next_node_id(node_id, edge_list)
    }
    return note
    