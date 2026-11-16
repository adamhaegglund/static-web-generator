
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from utils.markdown_to_blocks import markdown_to_blocks
from utils.block_to_block import BlockType, block_to_block_type
from utils.text_to_nodes import text_to_textnodes

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children_nodes : list[HTMLNode] = []
    for block in blocks:
        block_type : BlockType = block_to_block_type(block)
        match block_type:
            case BlockType.CODE:
                if not block.startswith("```") or not block.endswith("```"):
                    raise ValueError("invalid code block")
                text = block[4:-3]
                raw_text_node = TextNode(text, TextType.CODE)
                node : LeafNode = text_node_to_html_node(raw_text_node)
                pnode : ParentNode = ParentNode("pre",[node])
                children_nodes.append(pnode)
            case BlockType.HEADING:
                heading, hashtag_amount = heading_type(block)
                splitted_heading = split_heading(block, hashtag_amount)
                pnode : ParentNode = ParentNode(heading, text_to_chilren(splitted_heading))
                children_nodes.append(pnode)
            case BlockType.ORDERED_LIST:
                items = block.split("\n")
                html_items = []
                for item in items:
                    parts = item.split(". ", 1)
                    text = parts[1]
                    children = text_to_chilren(text)
                    html_items.append(ParentNode("li", children))
                children_nodes.append(ParentNode("ol", html_items))
            case BlockType.UNORDERED_LIST:
                items = block.split("\n")
                html_items = []
                for item in items:
                    text = item[2:]
                    children = text_to_chilren(text)
                    html_items.append(ParentNode("li", children))
                children_nodes.append(ParentNode("ul", html_items))
            case BlockType.QUOTE:
                lines = block.split("\n")
                new_lines = []
                for line in lines: 
                    if not line.startswith(">"):
                        raise ValueError("invalid quote block")
                    new_lines.append(line.lstrip(">").strip())
                content = " ".join(new_lines)
                children = text_to_chilren(content)
                children_nodes.append(ParentNode("blockquote", children))
            case BlockType.PARAGRAPH:
                lines = block.split('\n')
                paragraph = " ".join(lines)
                pnode : ParentNode = ParentNode("p", text_to_chilren(paragraph))
                children_nodes.append(pnode)

    parent_node = ParentNode(tag="div", children=children_nodes)
    return parent_node

def text_to_chilren(text: str) -> list[HTMLNode]:
    html_node_list : list[HTMLNode] = []
    tn_list: list[TextNode] = text_to_textnodes(text)
    for tn in tn_list:
        html_node = text_node_to_html_node(tn)
        html_node_list.append(html_node)
    return html_node_list

def heading_type(text: str) -> tuple[str, int]:
    hashtags = text.split()[0]
    hashtag_amount = hashtags.count("#")
    if hashtag_amount > 6:
        raise Exception("Too many hashtags for heading. Needs to be 1-6")
    return (f"h{hashtag_amount}", hashtag_amount)

def split_heading(text: str, hashtag_amount: int) -> str:
    return text[hashtag_amount +1:]

