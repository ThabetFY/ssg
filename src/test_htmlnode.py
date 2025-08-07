import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        tag = "h1"
        value = "Hello Word!"
        children = None
        props = {"class": "greeting", "href": "https://boot.dev"}
        node = HTMLNode(tag, value, children, props)
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values_exist(self):
        tag = "dev"
        value = "this is a dev"
        children = [HTMLNode("<h2>", "this is a heading")]
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode(tag, value, children, props)
        self.assertEqual(tag, node.tag)
        self.assertEqual(value, node.value)
        self.assertEqual(children, node.children)
        self.assertEqual(props, node.props)

    def test_args_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )


class TestLeafNode(unittest.TestCase):
    def test_to_html_props(self):
        tag = "h1"
        value = "Hello Word!"
        props = {"class": "greeting", "href": "https://boot.dev"}
        node = LeafNode(tag, value, props)
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_leaf_to_html_p(self):
        tag = "h1"
        value = "Hello Word!"
        node = LeafNode(tag, value)
        self.assertEqual(
            node.to_html(),
            "<h1>Hello Word!</h1>",
        )

    def test_values_exist(self):
        tag = "dev"
        value = "this is a dev"
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = LeafNode(tag, value, props)
        self.assertEqual(tag, node.tag)
        self.assertEqual(value, node.value)
        self.assertEqual(props, node.props)

    def test_props_none(self):
        tag = "dev"
        value = "this is a dev"
        node = LeafNode(tag, value)
        self.assertIsNone(node.props)

    def test_repr(self):
        node = LeafNode(
            "p",
            "What a strange world",
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )


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

    def test_to_html_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(
            "div", [child_node], {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            parent_node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_repr(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.__repr__(),
            "HTMLNode(div, None, [HTMLNode(span, child, None, None)], None)",
        )


if __name__ == "__main__":
    unittest.main()
