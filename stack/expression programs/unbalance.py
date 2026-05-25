# balance the unbalanced expression evaluation code
stack = []
expression = input("Enter an expression: ")
open=0
close=0
for char in expression:
    if char=='(':
        open+=1
    elif char==')':
        if open>0:
            open-=1
        else:
            close+=1
balanced_expression = ')' * close + expression + '(' * open
print("Balanced expression:", balanced_expression)