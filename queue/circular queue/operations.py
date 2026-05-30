# # operations on circular queue
# size=int(input("Enter the size of the circular queue: "))
# cq=circularqueue(size)
# while True:
#     print("1. Enqueue")
#     print("2. Dequeue")
#     print("3. Display")
#     print("4. Exit")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         data=int(input("Enter the data to enqueue: "))
#         cq.enqueue(data)
#     elif choice==2:
#         cq.dequeue()
#     elif choice==3:
#         cq.display()
#     elif choice==4:
#         break
#     else:
#         print("Invalid choice! Please try again.")


# operations on circular queue
class circularqueue:
    def __init__(self, size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def enqueue(self, data):
        if (self.rear+1)%self.size==self.front:
            print("Queue is full! Cannot enqueue.")
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
            print("Enqueued:", data)
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
            print("Enqueued:", data)
    def dequeue(self):
        if self.front==-1:
            print("Queue is empty! Cannot dequeue.")
        elif self.front==self.rear:
            print("Dequeued:", self.queue[self.front])
            self.front=-1
            self.rear=-1
        else:
            print("Dequeued:", self.queue[self.front])
            self.front=(self.front+1)%self.size
    def display(self):
        if self.front==-1:
            print("Queue is empty!")
        else:
            result=[]
            if self.rear>=self.front:
                for i in range(self.front, self.rear+1):
                    result.append(self.queue[i])
            else:
                for i in range(self.front, self.size):
                    result.append(self.queue[i])
                for i in range(0, self.rear+1):
                    result.append(self.queue[i])
            result.append(result[0])  # To show the circular nature
            print("Circular Queue:", " -> ".join(map(str, result)))
size=int(input("Enter the size of the circular queue: "))
cq=circularqueue(size)
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        data=int(input("Enter the data to enqueue: "))
        cq.enqueue(data)
    elif choice==2:
        cq.dequeue()
    elif choice==3:
        cq.display()
    elif choice==4:
        break
    else:
        print("Invalid choice! Please try again.")