import unittest
import htmlnode
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_url(self):
        node = TextNode("this is a text node", TextType.LINK, "https://www.google.com")
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.tag, "a")
        self.assertEqual(htmlnode.props, {"href": "https://www.google.com"})
if __name__ == "__main__":
    unittest.main()


