import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        prop_node_1 = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        prop_node_2 = None
        prop_node_3 = None 

        node = HTMLNode("a", None, None, prop_node_1 )
        node2 = HTMLNode("p", "This is a test node", )
        node3 = HTMLNode("ul", None, [HTMLNode("li"), HTMLNode("li")], None)
        node.props_to_html()
        node2.props_to_html()
        node3.props_to_html()

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertEqual(node2.props_to_html(), "")
        self.assertEqual(node3.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, Google!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, Google!</a>')

if __name__ == "__main__":
    unittest.main()
