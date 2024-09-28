import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
    text_node_to_html_node
    )

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, bold, https://www.boot.dev)", node.__repr__())


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_eq(self):
        text_node = TextNode("This is a text node", "bold")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
    
    def test_not_eq(self):
        text_node = TextNode("This is a text node", "bold")
        html_node = text_node_to_html_node(text_node)
        self.assertNotEqual(html_node.tag, "h1")
    
    def test_two(self):
        text_node = TextNode("This is a text node", "bold")
        html_node = text_node_to_html_node(text_node)
        text_node2 = TextNode("This is a text node", "bold")
        html_node2 = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), html_node2.to_html())


if __name__ == "__main__":
    unittest.main()