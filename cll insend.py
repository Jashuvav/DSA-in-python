'''circular linked list insertion at end'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
n= int(input("Enter the number of nodes: "))
for i in range(n):
    val= int(input("Enter data for node {}: ".format(i+1)))
    new_node= Node(val)
    if head is None:
        head = new_node
        new_node.next = head
    else:
        temp = head
        while temp.next != head:
            temp = temp.next
        temp.next = new_node
        new_node.next = head
temp = head
while temp.next != head:
    print(temp.data, end=" -> ")
    temp = temp.next
print(temp.data, end=" -> ")
print(head.data)                       

