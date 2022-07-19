result = ''
stack = []
cond = False

string = str(input())

for s in string:
    if s == '<':
        cond = True
        while stack:
            result += stack.pop()
        result += s
    elif s == '>':
        cond = False
        result += s
    elif s == ' ':
        if cond:
            result += s
        else:
            while stack:
                result += stack.pop()
            result += ' '
    elif s != ' ':
        if cond:
            result += s
        else:
            stack.append(s)

while stack:
    result += stack.pop()

print(result)
