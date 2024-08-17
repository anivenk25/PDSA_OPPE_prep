class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

def insert_element(root, k):
    if k < root.data:
        if root.left is None:
            root.left = Node(k)
        else:
            insert_element(root.left, k)
    elif k > root.data:
        if root.right is None:
            root.right = Node(k)
        else:
            insert_element(root.right, k)

