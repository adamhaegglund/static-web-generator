from textnode import TextNode, TextType
from utils.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text: str) -> list[TextNode]:
    new_node = TextNode(text, TextType.TEXT)
    bold_delimeter = split_nodes_delimiter([new_node], "**", TextType.BOLD)
    italic_delimeter =split_nodes_delimiter(bold_delimeter, "_", TextType.ITALIC)
    code_delimeter = split_nodes_delimiter(italic_delimeter, "`", TextType.CODE)
    images = split_nodes_image(code_delimeter)
    final = split_nodes_link(images)
    return final
