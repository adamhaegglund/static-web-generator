from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list : list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_list.append(old_node)
        else:
            split_list = old_node.text.split(delimiter)
            if len(split_list) % 2 == 0:
                raise Exception("Missing end delimiter for the node in provided node")
            for i,v in enumerate(split_list):
                if v == "":
                    continue
                if i % 2 == 1:
                    new_list.append(TextNode(v, text_type))
                else:
                    if v == "":
                        continue
                    new_list.append(TextNode(v, TextType.TEXT))
    return new_list
