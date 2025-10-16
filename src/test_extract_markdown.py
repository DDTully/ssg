import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        text = "![one](url1.png) and ![two](url2.jpg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("one", "url1.png"), ("two", "url2.jpg")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is a [link](https://boot.dev)")
        self.assertListEqual([("link", "https://boot.dev")], matches)

    def test_extract_multiple_links(self):
        text = "[one](url1) and [two](url2)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("one", "url1"), ("two", "url2")], matches)

    def test_images_and_links_together(self):
        text = "![alt](img.png) and [boot](https://boot.dev)"
        images = extract_markdown_images(text)
        links = extract_markdown_links(text)
        self.assertListEqual([("alt", "img.png")], images)
        self.assertListEqual([("boot", "https://boot.dev")], links)

    def test_no_matches(self):
        self.assertEqual(extract_markdown_images("just text"), [])
        self.assertEqual(extract_markdown_links("just text"), [])


if __name__ == "__main__":
    unittest.main()
