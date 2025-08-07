import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a diffrent text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_values_exist(self):
        text = "This is a node's url should be none"
        text_type = TextType.TEXT
        url = "https://www.boot.dev"
        node = TextNode(text, text_type, url)
        self.assertEqual(text, node.text)
        self.assertEqual(text_type, node.text_type)
        self.assertEqual(url, node.url)

    def test_url_none(self):
        node = TextNode("This is a node's url should be none", TextType.TEXT)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
