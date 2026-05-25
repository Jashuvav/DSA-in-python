# # queue Data Structure: FIFO (First In First Out) 
# # Enqueue: Add an item to the rear of the queue
# # Dequeue: Remove an item from the front of the queue

# # enqueue operation
# queue = []
# n= int(input("Enter the number of elements to enqueue: "))
# for i in range(n):
#     val=int(input("Enter element {}: ".format(i+1)))
#     queue.append(val)
# print("Queue after enqueue operations:", queue)

# # dequeue operation
# m = int(input("Enter the number of elements to dequeue: "))
# for i in range(m):
#     if len(queue)== 0:
#         print("Queue is overflow")
#     elif queue:
#         print("Dequeued element:", queue.pop(0))
#     else:
#         print("Queue is empty")
# print("Queue after dequeue operations:", queue)

# # peek operation
# if queue:
#     print("Front element (peek):", queue[0])    
# else:
#     print("Queue is empty, no front element to peek.")


# # queue using single linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#     def enqueue(self, data):
#         new_node = Node(data)
#         if self.rear is None:
#             self.front = self.rear = new_node
#             return
#         self.rear.next = new_node
#         self.rear = new_node
#     def dequeue(self):
#         if self.front is None:
#             print("Queue is empty")
#             return None
#         temp = self.front
#         self.front = temp.next
#         if self.front is None:
#             self.rear = None
#         return temp.data
#     def peek(self):
#         if self.front is not None:
#             return self.front.data
#         else:
#             print("Queue is empty, no front element to peek.")
#             return None
# # Example usage
# queue = Queue()
# n = int(input("Enter the number of elements to enqueue: "))
# for i in range(n):
#     val = int(input("Enter element {}: ".format(i+1)))
#     queue.enqueue(val)
# print("Queue after enqueue operations:")
# temp = queue.front
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")
# m = int(input("Enter the number of elements to dequeue: "))
# for i in range(m):
#     dequeued_element = queue.dequeue()
#     if dequeued_element is not None:
#         print("Dequeued element:", dequeued_element)
# print("Queue after dequeue operations:")
# temp = queue.front
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")
# peeked_element = queue.peek()
# if peeked_element is not None:
#     print("Front element (peek):", peeked_element)


# list=[2,4,5,6,3,2,3,4]
# evem=[]
# odd=[]
# for i in range(len(list)):
#     if i%2==0:
#         evem.append(list[i])
#     else:
#         odd.append(list[i])
# a=sum(evem)
# b=sum(odd)
# diff=abs(a-b)
# print(diff)


# list=[-2,-5,6,-1,3]
# evem=[]
# odd=[]
# for i in range(len(list)):
#     if i%2==0:
#         evem.append(list[i])
#     else:
#         odd.append(list[i])
# a=sum(evem)
# b=sum(odd)
# diff=abs(a-b)
# print(diff)

a=[-2,-5,6,-1,3]
evem=[]
for i in a:
    if i<0:
        evem.append(i)
print(sum(evem))

# in the even num highest num and in the odd num lowest num sum of both
b=[-2,-5,6,-1,3,-4,-6]
even=[]
odd=[]
for i in b:
    if i>0:
        if i%2==0:
            even.append(i)
            print(even)
    elif i<0:
        if i%2!=0:
            odd.append(i)
            print(odd)
a=max(even)
c=min(odd)
print(a+c)