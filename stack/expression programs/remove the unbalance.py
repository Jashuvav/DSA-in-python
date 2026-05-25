# remove the unbalance parentheses
expression = input("Enter an expression: ")
stack = []
removePos=set()
for i in range(len(expression)):
    ch=expression[i]
    if ch == '(':
        stack.append(i)
    elif ch == ')':
        if stack:
            stack.pop()
        else:
            removePos.add(i)
while stack:
    removePos.add(stack.pop())
result=' '
for i in range(len(expression)):
    if i not in removePos:
        result+=expression[i]
print("Expression after removing unbalanced parentheses:", result.strip())