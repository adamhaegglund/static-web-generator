import unittest
from utils.block_to_block import block_to_block_type, BlockType

class TestBlockToBlock(unittest.TestCase):
    def test_heading(self):
        text = "### This is heading 3"
        text2 = "# This is heading 1"
        text3 ="#This should be a paragraph"

        self.assertEqual(block_to_block_type(text), BlockType.HEADING)
        self.assertEqual(block_to_block_type(text2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(text3), BlockType.PARAGRAPH)

    def test_code(self):
        text = "```This is a codeblock```"

        self.assertEqual(block_to_block_type(text), BlockType.CODE)

    def test_quote(self):
        text = "> Quote\n> With \n> Multiple \n> Lines"

        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)
    def test_ul(self):
        text ="- Item 1\n- Item 2"

        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)
    def test_ol(self):
        text = "1. Item1\n2. Item 2"

        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)
    def test_p(self):
        text = "This is just a simple paragraph"

        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
