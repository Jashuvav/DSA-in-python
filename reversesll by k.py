'''reverse a singly linked list by k nodes'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head
def reverse_k_nodes(head, k):
    prev = None
    current = head
    count = 0
    while current and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1
    if next_node:
        head.next = reverse_k_nodes(next_node, k)
    return prev
def display(head):
    if head is None:
        print("List is empty.")
        return
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("tail")
head = None
n = int(input("Enter the number of nodes: "))
for i in range(n):
    data = int(input("Enter data for node {}: ".format(i+1)))
    head = insert_end(head, data)
k = int(input("Enter the value of k: "))
print("Linked List before reversal:")
display(head)
head = reverse_k_nodes(head, k)
print("Linked List after reversal by k nodes:")
display(head)
