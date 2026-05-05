#insert at begin and delete at end
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def delete_end(head):
    if head is None:
        print("List is empty.")
        return None
    if head.next is None:
        print("List has only one node. Deleting the node.")
        return None
    temp = head
    while temp.next.next:
        temp = temp.next
        print("Deleting node with data:", temp.next.data)
    temp.next = None
    return head
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
    head = insert_begin(head, data)
print("Linked List after insertion at the beginning:")
display(head)
head = delete_end(head)
print("Linked List after deletion at the end:")
display(head)
