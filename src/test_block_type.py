import unittest
from block_type import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Six"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_block_type("```\ncode here\n```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> quote\n> again"), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- item1\n- item2\n- item3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. one\n2. two\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Just normal text"), BlockType.PARAGRAPH)

    def test_invalid_heading(self):
        self.assertEqual(block_to_block_type("####### too many"), BlockType.PARAGRAPH)

    def test_ordered_list_wrong_numbers(self):
        block = "1. one\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
