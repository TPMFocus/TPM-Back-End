def get_next_node_id(node_id, edge_list):
    next_node = []
    for edge in edge_list:
        if edge["source"] == "{}".format(node_id):
            next_node.append(edge["target"])
    return next_node