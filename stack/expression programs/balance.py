# expression evaluation code
stack = []
expression = input("Enter an expression: ")
for char in expression:
    if char in '({[':
        stack.append(char)
    elif char in ')}]':
        if not stack:
            print("Unbalanced parentheses")
            break
        top = stack.pop()
        if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
            print("Unbalanced parentheses")
            break   
else:
    if not stack:
        print("Balanced parentheses")
    else:
        print("Unbalanced parentheses")