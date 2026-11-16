import unittest

from utils.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_strips_whitespace(self):
        self.assertEqual(extract_title("#   Hello world   "), "Hello world")

    def test_title_not_first_line(self):
        md = "Some intro\n\n## Sub\n\n# The Title\n\nBody"
        self.assertEqual(extract_title(md), "The Title")

    def test_ignores_h2(self):
        with self.assertRaises(ValueError):
            extract_title("## Not a title\n\ntext")

    def test_no_title(self):
        with self.assertRaises(ValueError):
            extract_title("just a paragraph")


if __name__ == "__main__":
    unittest.main()
