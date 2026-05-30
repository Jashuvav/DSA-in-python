class Stack:
    """
    Stack implementation using a Python list (array).
    Supports push, pop, and isEmpty operations.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, value):
        """
        Add an element to the top of the stack.
        
        Args:
            value: The value to be added to the stack.
        
        Time Complexity: O(1) - amortized constant time
        """
        self.items.append(value)
    
    def pop(self):
        """
        Remove and return the top element from the stack.
        
        Returns:
            The value at the top of the stack.
        
        Raises:
            IndexError: If the stack is empty.
        
        Time Complexity: O(1)
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def isEmpty(self):
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        
        Time Complexity: O(1)
        """
        return len(self.items) == 0
    
    def peek(self):
        """
        Return the top element without removing it.
        
        Returns:
            The value at the top of the stack.
        
        Raises:
            IndexError: If the stack is empty.
        
        Time Complexity: O(1)
        """
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def size(self):
        """
        Return the number of elements in the stack.
        
        Returns:
            The size of the stack.
        
        Time Complexity: O(1)
        """
        return len(self.items)
    
    def display(self):
        """
        Display all elements in the stack from top to bottom.
        
        Time Complexity: O(n)
        """
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack (top to bottom):", self.items[::-1])


# Testing the Stack implementation
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()
    
    # Test isEmpty on empty stack
    print("Is stack empty?", stack.isEmpty())  # Output: True
    
    # Test push operation
    print("\nPushing elements: 10, 20, 30, 40")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
    # Display stack
    stack.display()  # Output: Stack (top to bottom): [40, 30, 20, 10]
    
    # Test isEmpty on non-empty stack
    print("Is stack empty?", stack.isEmpty())  # Output: False
    
    # Test size
    print("Stack size:", stack.size())  # Output: 4
    
    # Test peek
    print("Top element (peek):", stack.peek())  # Output: 40
    
    # Test pop operation
    print("\nPopping elements:")
    print("Popped:", stack.pop())  # Output: 40
    print("Popped:", stack.pop())  # Output: 30
    stack.display()  # Output: Stack (top to bottom): [20, 10]
    
    # Pop remaining elements
    print("Popped:", stack.pop())  # Output: 20
    print("Popped:", stack.pop())  # Output: 10
    
    # Test isEmpty on empty stack
    print("Is stack empty?", stack.isEmpty())  # Output: True
    
    # Test error handling
    print("\nTrying to pop from empty stack:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error caught: {e}")
