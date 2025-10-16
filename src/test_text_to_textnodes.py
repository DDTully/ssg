import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_only_text(self):
        text = "Just normal text"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("Just normal text", TextType.TEXT)])

    def test_only_bold(self):
        text = "**bold**"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("bold", TextType.BOLD)])

    def test_only_italic(self):
        text = "_italic_"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("italic", TextType.ITALIC)])

    def test_only_code(self):
        text = "`code`"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("code", TextType.CODE)])

    def test_only_image(self):
        text = "![alt](url)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("alt", TextType.IMAGE, "url")])

    def test_only_link(self):
        text = "[link](url)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("link", TextType.LINK, "url")])


if __name__ == "__main__":
    unittest.main()
