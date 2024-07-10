from app.utils.ConvertScript.Structure import *
from app.utils.ConvertScript.Extract import *
import json

def build(json_data_list):
    try:
        # Extracting the next nodes
        next_nodes = extract_next_nodes(json_data_list)
    except Exception as e:
        print('Error extracting next nodes : ', e)
        return
    try:
        # Extracting the node data
        node_data = extract_node_data(json_data_list)
    except Exception as e:
        print('Error extracting node data : ', e)
        return
    try:
        # Extracting the node types
        node_types = extract_node_types(json_data_list)
    except Exception as e:
        print('Error extracting node types : ', e)
        return
    try:
        # Combine the node types and the node data into a single dictionary
        node_types_data = []
        for node_type in node_types:
            for node_datum in node_data:
                if node_type["node_id"] == node_datum["node_id"]:
                    node_types_data.append({"node_id": node_type["node_id"], "node_type": node_type["node_type"], "data": node_datum["data"]})
    except Exception as e:
        print('Error combining node types and node data : ', e)
        return
    
    #print('\nnode_types_data:', json.dumps(node_types_data), '\n')
    # Creating the structure
    final_structure_node = []
    final_structure_edge = []

    try:
        for node in node_types_data:
            node = json.loads(json.dumps(node))
            #print('node:', node, '\n')
            try:
                structure = generate_node_structure(node)
            except Exception as e:
                print('Error generating node structure initially : ', e)
                return
            #print('structure:', json.dumps(structure), '\n')
            try:
                structure['data']['inputs'] = node['data']
                final_structure_node.append(structure)
            except Exception as e:
                print('Error generating node structure 2nd : ', e)
                return
    except Exception as e:
        print('Error generating node structure : ', e)
        return
    
    try:
        for node in next_nodes:
            for next_node in node["next_node"]:
                #print('next_node:', json.dumps(next_node), '\n')
                source = [n for n in node_types_data if n["node_id"] == node["node_id"]][0]
                #print('source:', json.dumps(source), '\n')
                target = [i for i in node_types_data if i["node_id"] == next_node][0]
                #print('target:', json.dumps(target), '\n')
                final_structure_edge.append(generate_edge_structure(source, target))
    except Exception as e:
        print('Error generating edge structure : ', e)
        return
    return final_structure_node, final_structure_edge