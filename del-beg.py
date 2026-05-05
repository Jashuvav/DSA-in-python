#insert at begin and delete at begin
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def delete_begin(head):
    if head is None:
        print("List is empty.")
        return None
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
    head = insert_begin(head, data)
print("Linked List after insertion at the beginning:")
display(head)
head = delete_begin(head)
print("Linked List after deletion at the beginning:")
display(head)
