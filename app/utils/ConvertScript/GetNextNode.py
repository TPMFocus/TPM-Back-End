def get_next_node_id(node_id, edge_list):
    next_node = []
    for edge in edge_list:
        if edge["source"] == "{}".format(node_id):
            next_node.append(edge["target"])
    return next_node

def extract_int(string):
  """
  Extracts the int value from a string containing an int at the end.

  Args:
      string: The string to extract the int value from.

  Returns:
      The extracted int value, or None if no int is found.
  """

  digits = ""
  for char in string[::-1]:
    if char.isdigit():
      digits += char
    else:
      break
  return int(digits[::-1]) if digits else None