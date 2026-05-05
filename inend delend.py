#insert at end and delete at end
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
    head = insert_end(head, data)
print("Linked List after insertion at the end:")
display(head)
head = delete_end(head)
print("Linked List after deletion at the end:")
display(head)
