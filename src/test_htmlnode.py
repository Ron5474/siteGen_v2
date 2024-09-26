import unittest

from htmlnode import HTMLNode

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



if __name__ == "__main__":
    unittest.main()