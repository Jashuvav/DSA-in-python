# dequemethods
'''
Methods for working with deques.
    1. append(x) - Add x to the right side of the deque.
    2. appendleft(x) - Add x to the left side of the deque.
    3. clear() - Remove all elements from the deque.
    4. copy() - Create a shallow copy of the deque.
    5. count(x) - Count the number of deque elements equal to x.
    6. extend(iterable) - Extend the right side of the deque by appending elements from the iterable argument.
    7. extendleft(iterable) - Extend the left side of the deque by appending elements from the iterable argument (note: the series of left appends results in reversing the order of elements in the iterable argument).
    8. index(x[, start[, stop]]) - Return the position of the first occurrence of x in the deque (at or after index start and before index stop). Raises ValueError if not found.
    9. insert(i, x) - Insert x into the deque at position i. If i is greater than the length of the deque, x is appended to the right side.
    10. pop() - Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.
    11. popleft() - Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.
    12. remove(value) - Remove the first occurrence of value. Raises ValueError if not found.
    13. reverse() - Reverse the elements of the deque in-place and then return None.
    14. rotate(n=1) - Rotate the deque n steps to the right. If n is negative, rotate to the left.

'''



from collections import deque
d=deque()
d.append(1)
d.append(2)
d.append(3)
print(d)
d.appendleft(0)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.extend([4,5,6])
print(d)
d.extendleft([4,-2,-3])
print(d)
d.remove(4) # removes the first occurrence of 4
print(d)
d.reverse()
print(d)
d.rotate(2)  # Rotate 2 steps to the right
print("Rotated right by 2:", d)
d.rotate(-3) # Rotate 3 steps to the left
print("Rotated left by 3:", d)
