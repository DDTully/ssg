import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        children = [
            LeafNode("b", "Bold"),
            LeafNode(None, " text "),
            LeafNode("i", "Italic"),
        ]
        parent_node = ParentNode("p", children)
        self.assertEqual(parent_node.to_html(), "<p><b>Bold</b> text <i>Italic</i></p>")

    def test_to_html_nested_parents(self):
        nested = ParentNode(
            "section", [ParentNode("div", [LeafNode("span", "deep text")])]
        )
        self.assertEqual(
            nested.to_html(), "<section><div><span>deep text</span></div></section>"
        )

    def test_no_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "text")])

    def test_no_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])


if __name__ == "__main__":
    unittest.main()
