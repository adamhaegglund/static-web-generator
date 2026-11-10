import unittest

from textnode import TextType, TextNode
from utils.split_nodes import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes2 = split_nodes_delimiter([node2], "`", TextType.CODE)        
        self.assertEqual(new_nodes, 
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )
        self.assertEqual(new_nodes2, 
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
            ]
        )
    def test_split_nodes_bold(self):
        node = TextNode("**This word** is bold", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, 
            [
                TextNode("This word", TextType.BOLD),
                TextNode(" is bold", TextType.TEXT),
            ]
        )

if __name__ == "__main__":
    unittest.main()


