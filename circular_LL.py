#circular single linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        new_node.next = new_node
        return new_node
    temp = head
    while temp.next != head:
        temp = temp.next
    temp.next = new_node
    new_node.next = head
    return head
def delete_beg(head):
    if head is None:
        print("CLL is empty")
        return None
    if head.next == head:
        return None 
    temp = head
    while temp.next != head:
        temp = temp.next
    temp.next = head.next
    head = head.next
    return head
def display(head):
    if head is None:
        print("CLL is empty")
        return
    temp = head
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == head:
            break
    print("head")

head = None
n = int(input("Enter the number of nodes: "))
for i in range(n):
    data = int(input("Enter data for node {}: ".format(i+1)))
    head = insert_end(head, data)
print("Circular Linked List before deletion:")
display(head)
head = delete_beg(head)
print("Circular Linked List after deletion at beginning:")
display(head)
