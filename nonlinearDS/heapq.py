# heap queue implementation
# heapq methods:
# heapq.heapify(x) - transforms list x into a heap, in-place, in
# heapq.heappush(heap, item) - pushes the value item onto the heap, maintaining the heap invariant.
# heapq.heappop(heap) - pops and returns the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised.
# heapq.heappushpop(heap, item) - pushes the new item on the heap, then pops and returns the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().
# heapq.heapreplace(heap, item) - pops and returns the smallest item from the heap, and then pushes the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised. This is more efficient than heappop() followed by heappush().
# heapq.nlargest(n, iterable, key=None) - Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower).
# heapq.nsmallest(n, iterable, key=None) - Return a list with the n smallest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower).
import heapq
# create a min-heap from a list
min_heap = [3, 1, 4, 1, 5,              9]
heapq.heapify(min_heap) 
print("Min-Heap:", min_heap) # Min-Heap: [1, 1, 4, 3, 5, 9]
# push an item onto the heap
heapq.heappush(min_heap, 2)
print("Min-Heap after push:", min_heap) # Min-Heap after push: [1, 1, 2, 3, 5, 9, 4]
# pop the smallest item from the heap
smallest = heapq.heappop(min_heap)
print("Popped smallest item:", smallest) # Popped smallest item: 1
print("Min-Heap after pop:", min_heap) # Min-Heap after pop: [1, 3, 2, 4, 5, 9]
# push an item and pop the smallest item in one operation
smallest = heapq.heappushpop(min_heap, 0)
print("Pushed 0 and popped smallest item:", smallest) # Pushed 0 and
print("Min-Heap after pushpop:", min_heap) # Min-Heap after pushpop: [0, 3, 2, 4, 5, 9]
# pop the smallest item and push a new item in one operation
smallest = heapq.heapreplace(min_heap, 6)
print("Popped smallest item and pushed 6:", smallest) # Popped smallest item and pushed 6: 0
