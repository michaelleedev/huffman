import unittest
import main
from node import node


class TestExtractData(unittest.TestCase):
    def test_create_tree(self):
        # check root character
        dict = {"a": 0, "b": 1, "d": 3, "c": 2}
        root = main.create_tree(dict)
        y = root.char
        self.assertEqual('d', root.char)

        # check tree integrity
        s = 'abbccdd'
        traverse = self.tree_traverse(root)
        self.assertEqual(s, traverse)

    # traverses tree inorder and returns a string of characters in each node
    def tree_traverse(self, root):
        if(root.left is None and root.right is None):
            return root.char
        elif(root.left is None):
            return root.char + self.tree_traverse(root.right)
        else:
            return self.tree_traverse(root.left) + root.char + self.tree_traverse(root.right)



if __name__ == "__main__":
    unittest.main()
