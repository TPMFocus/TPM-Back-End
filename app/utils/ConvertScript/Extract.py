from app.utils.ConvertScript.Structure import *
import json

def extract_next_nodes(json_data_list):
    next_nodes = []
    for json_data in json_data_list:
        try:
            data = json_data
            node_id = data.get("node_id")
            next_node = data.get("next_node", [])
            next_nodes.append({"node_id": node_id, "next_node": next_node})
        except json.JSONDecodeError:
            next_nodes.append({})
    return next_nodes

def extract_node_data(json_data_list):
    node_datas = []
    for json_data in json_data_list:
        try:
            data = json_data
            node_id = data.get("node_id")
            node_data = data.get("data", {})
            node_datas.append({"node_id": node_id, "data": node_data})
        except json.JSONDecodeError:
            node_datas.append({})
    return node_datas

def extract_node_types(json_data_list):
    node_types = []
    for json_data in json_data_list:
        try:
            data = json_data
            node_id = data.get("node_id")
            node_type = data.get("node")
            node_types.append({"node_id": node_id, "node_type": node_type})
        except json.JSONDecodeError:
            node_types.append({})
    return node_types

def extract_json_data():
    file_path = '/home/adam_skandrani/tpm_back/tmp/json_response.json'
    with open(file_path) as f:
        json_data = f.read()
    return json_data