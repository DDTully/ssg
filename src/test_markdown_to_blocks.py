import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_and_whitespace_blocks(self):
        md = """
        
This is text



Another block

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is text", "Another block"])

    def test_single_block(self):
        md = "Only one block here"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Only one block here"])


if __name__ == "__main__":
    unittest.main()
