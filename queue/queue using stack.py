# queue using stack


s1 = []
s2 = []
def enqueue():
    element = int(input("Enter the element to enqueue: "))
    s1.append(element)
    print(f"Enqueued {element} to the queue.")
def dequeue():
    if not s1 and not s2:
        print("Queue is empty. Cannot dequeue.")
        return
    if not s2:
        while s1:
            s2.append(s1.pop())
    removed = s2.pop()
    print(f"Dequeued {removed} from the queue.")
def display():
    if not s1 and not s2:
        print("Queue is empty.")
        return
    queue_elements = s2[::-1] + s1
    print("Queue elements:", queue_elements)
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
       enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


# queue operations using deque
from collections import deque
q=deque()
def enqueue():
    element = int(input("Enter the element to enqueue: "))
    q.append(element)
    print(f"Enqueued {element} to the queue.")
def dequeue():
    if not q:
        print("Queue is empty. Cannot dequeue.")
        return
    removed = q.popleft()
    print(f"Dequeued {removed} from the queue.")
def display():
    if not q:
        print("Queue is empty.")
        return
    print("Queue elements:", list(q))
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
       enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        