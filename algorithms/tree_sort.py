class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(node, arr, highlights):
    if node:
        yield from inorder(node.left, arr, highlights)
        highlights.append(len(arr))
        arr.append(node.val)
        yield arr, highlights.copy()
        highlights.pop()
        yield from inorder(node.right, arr, highlights)

def tree_sort(arr):
    root = None
    for val in arr:
        root = insert(root, val)
    arr.clear()
    highlights = []
    yield from inorder(root, arr, highlights)
