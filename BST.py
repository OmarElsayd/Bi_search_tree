class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = Node(root)

    def left_insert(self, data, pos):
        if pos.left is None:
            pos.left = Node(data)
        else:
            pos = pos.left
            if data < pos.data:
                self.left_insert(data, pos)
            else:
                self.right_insert(data, pos)

    def right_insert(self, data, pos):
        if pos.right is None:
            pos.right = Node(data)
        else:
            pos = pos.right
            if data < pos.data:
                self.left_insert(data, pos)
            else:
                self.right_insert(data, pos)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        elif data < self.root.data:
            self.left_insert(data, self.root)
        else:
            self.right_insert(data, self.root)
                
if __name__ == "__main__":
    tree = BST(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(17)