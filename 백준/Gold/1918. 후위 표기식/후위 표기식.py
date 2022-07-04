import sys
import string

operand = string.ascii_uppercase
infixs = list(sys.stdin.readline().strip())

operator_stack = []
result = ""
temp_stack = []
for infix in infixs:
    if infix in operand:
        result += infix
    elif infix == "(":
        operator_stack.append("(")
    elif infix == ")":
        while operator_stack:
            if operator_stack[-1] != "(":
                result += operator_stack.pop()
            else:
                operator_stack.pop()
                break
        while operator_stack:
            if operator_stack[-1] in ["*", "/"]:
                result += operator_stack.pop()
            else:
                break
    elif infix in ["*", "/"]:
        if operator_stack and operator_stack[-1] in ["*", "/"]:
            result += operator_stack.pop()
        operator_stack.append(infix)
    elif infix in ["+", "-"]:
        while operator_stack:
            if operator_stack[-1] != "(":
                result += operator_stack.pop()
            else:
                break
        operator_stack += [infix]


while operator_stack:
    result += operator_stack.pop()

print(result)