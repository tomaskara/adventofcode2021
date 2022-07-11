with open('input.txt') as f:
    data = f.read().splitlines()

dic_of_nodes = {}

def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = [value]


for line in data:
    first_node, second_node = line.split("-")
    append_value(dic_of_nodes, first_node, second_node)
    append_value(dic_of_nodes, second_node, first_node)

for key, value in dic_of_nodes.items():
    if "end" in value:
        value.remove("end")
        value.append("end")
        dic_of_nodes[key] = value

final_paths = []


def find_path(starting_path):
    for connection in dic_of_nodes[starting_path[-1]]:
        if connection == "end":
            starting_path.append(connection)
            if starting_path not in final_paths:
                final_paths.append(starting_path)
            return
        if connection.islower():
            if connection in starting_path:
                pass
            else:
                new_list = starting_path.copy()
                new_list.append(connection)
                find_path(new_list)

        else:
            new_list = starting_path.copy()
            new_list.append(connection)
            find_path(new_list)


for i in dic_of_nodes['start']:
    find_path(['start', i])

print(len(final_paths))
