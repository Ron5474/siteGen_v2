import unittest

from htmlnode import HTMLNode, LeafNode

class TesthtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a html node")
        node2 = HTMLNode("p", "This is a html node")
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_not_equal(self):
        node = HTMLNode("h1", "This is a html node")
        node2 = HTMLNode("h2", "This is a html node")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode("p", "This is a html node")
        self.assertEqual("HTMLNode(p, This is a html node, None)", node.__repr__())
    
    def test_child(self):
        node2 = HTMLNode("h2", "This is a html node")
        node = HTMLNode("h1", "This is a html node", [node2])
        self.assertEqual(node.children[0], node2)

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a leaf node")
        node2 = LeafNode("p", "This is a leaf node")
        self.assertEqual(node.to_html(), node2.to_html())

    def test_not_equal(self):
        node = LeafNode("p", "This is a leaf node")
        node2 = LeafNode("a", "Boot.dev", {"href": "https://www.boot.dev"})
        self.assertNotEqual(node.to_html(), node2.to_html())

    
    def test_props(self):
        node = LeafNode("a", "Boot.dev", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), "<a href=https://www.boot.dev>Boot.dev</a>")




if __name__ == "__main__":
    unittest.main()