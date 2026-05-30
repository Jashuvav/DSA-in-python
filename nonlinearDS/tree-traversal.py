# in-order tree traversal
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)
values = list(map(int, input("Enter values to insert into the tree (space-separated): ").split()))
root = None
for value in values:
    root = insert(root, value)
print("In-order traversal of the tree:")
in_order_traversal(root)

# pre-order tree traversal
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
def pre_order_traversal(root):
    if root:
        print(root.value, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
values = list(map(int, input("Enter values to insert into the tree (space-separated): ").split()))
root = None
for value in values:
    root = insert(root, value)
print("Pre-order traversal of the tree:")
pre_order_traversal(root)



# post-order tree traversal
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root 
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=" ")
values = list(map(int, input("Enter values to insert into the tree (space-separated): ").split()))
root = None
for value in values:
    root = insert(root, value)
print("Post-order traversal of the tree:")
post_order_traversal(root)
