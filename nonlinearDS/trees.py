# tree DS diagram
# perfect binary tree
#     1 -> nodes
#    / \ -> edges
#   2   3 -> levels
#  / \ / \ -> branches
# 4  5 6  7  -> leaves

# proper binary tree
#     1
#    / \
#   2   3
# complete binary tree
#     1
#    / \
#   2   3
# binary search tree
#     4
#    / \
#   2   6       
#  / \ / \
# 1  3 5  7
# skewed binary tree
#     1
#    / \
#   2   3
#     \
#      4

# binary tree and node creation
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(root.value) # 1
print(root.left.value) # 2  
print(root.right.value) # 3
print(root.left.left.value) # 4
print(root.left.right.value) # 5
print(root.right.left.value) # 6    
print(root.right.right.value) # 7   


