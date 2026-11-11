from textnode import TextNode, TextType
from utils.extract_markdown_images import extract_markdown_images, extract_markdown_links

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
                    new_list.append(TextNode(v, TextType.TEXT))
    return new_list

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list : list[TextNode] = []
    for old in old_nodes:
        images = extract_markdown_images(old.text)
        if len(images) == 0:
            new_list.append(old)
            continue
        remaining_text = old.text
        for image_alt, image_url in images:
            before, remaining_text = remaining_text.split(f"![{image_alt}]({image_url})", 1)
            if before != "":
                new_list.append(TextNode(before, TextType.TEXT))
            new_list.append(TextNode(image_alt, TextType.IMAGE, image_url))
        if remaining_text != "":
            new_list.append(TextNode(remaining_text, TextType.TEXT))
    return new_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list : list[TextNode] = []
    for old in old_nodes:
        links = extract_markdown_links(old.text)
        if len(links) == 0:
            new_list.append(old)
            continue
        remaining_text = old.text
        for link_text, link_url in links:
            before, remaining_text = remaining_text.split(f"[{link_text}]({link_url})", 1)
            if before != "":
                new_list.append(TextNode(before, TextType.TEXT))
            new_list.append(TextNode(link_text, TextType.LINK, link_url))
        if remaining_text != "":
            new_list.append(TextNode(remaining_text, TextType.TEXT))
    return new_list





