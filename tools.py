import re


def hierarchical_to_dict(parent_name, data):
    tree = {}
    for d in data.keys():
        node = None
        for id in re.findall('..', d):
            current_dict = tree if node is None else node
            node = current_dict.get(id)
            if not node:
                node = {}
                current_dict[id] = node

    def walker(src, res, parent_id=''):
        for id, value in src.items():
            full_id = parent_id + id
            node = {'id': full_id, 'name': data[full_id]}
            if 'children' not in res:
                res['children'] = []
            res['children'].append(node)
            walker(value, node, parent_id + id)

    result = {'name': parent_name}
    walker(tree, result)
    return result
