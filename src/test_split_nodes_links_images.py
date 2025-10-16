import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link


class TestSplitNodesImagesLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_no_images(self):
        node = TextNode("Plain text no images", TextType.TEXT)
        self.assertListEqual([node], split_nodes_image([node]))

    def test_no_links(self):
        node = TextNode("Plain text no links", TextType.TEXT)
        self.assertListEqual([node], split_nodes_link([node]))

    def test_non_text_node_unchanged(self):
        node = TextNode("already link", TextType.LINK, "https://x.com")
        self.assertListEqual([node], split_nodes_link([node]))

    def test_image_at_start_and_end(self):
        node = TextNode("![first](url1) middle ![second](url2)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "url1"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("second", TextType.IMAGE, "url2"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
