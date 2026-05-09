#insert at end and delete at beginning of a double linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    new_node.prev = temp
    return head
def delete_beg(head):
    if head is None:
        print("DLL is empty")
        return None
    if head.next is None:
        return None 
    head=head.next
    head.prev=None
    return head
def display(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("tail")
head = None
n = int(input("Enter the number of nodes: "))
for i in range(n):
    data = int(input("Enter data for node {}: ".format(i+1)))
    head = insert_end(head, data)
print("Double Linked List before deletion:")
display(head)
head = delete_beg(head)
print("Double Linked List after deletion at beginning:")
display(head)