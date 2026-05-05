#insert at end and delete at beginning
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
def delete_begin(head):
    if head is None:
        print("List is empty.")
        return None
    print("Deleting node with data:", head.data)
    return head.next    
    
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
head = delete_begin(head)
print("Linked List after deletion at the beginning:")
display(head)
