'''linked list
example:
head -> 10|1000 -> 20|1008 -> 30|1016 -> tail
head -> 10|next -> 20|next -> 30|next -> tail
insert operation in a singly linked list:
H -> n1 -> n2 -> n3 -> tail
H -> 11 -> 22 -> 33 -> tail
insert from head:
input: 11
input: 22
input: 33
H -> 33 -> 22 -> 11 -> tail
insert from tail:
input: 11
input: 22
input: 33
H -> 11 -> 22 -> 33 -> tail
'''
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
def display(head):
    temp = head
    if temp is None:
        print("List is empty.")
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("tail")
head = None
n = int(input("Enter the number of nodes: "))   
for i in range(n):
    data = int(input("Enter data for node {}: ".format(i+1)))
    head = insert_end(head, data)
print("Linked List:")
display(head)
    