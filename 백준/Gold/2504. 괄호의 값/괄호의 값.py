'''
stack 문제 풀때
'''

string = input()
answer = 0

stack = []
for s in string:
    if not stack:
        if s == ')' or s == ']':
            break
        stack.append(s)
    else:
        temp_nums = []
        if s == ')':
            while stack and stack[-1] != '(' and stack[-1] != '[':
                temp_nums.append(stack.pop())

            if not stack:
                answer = 0
                stack.clear()
                break

            if stack[-1] == '(':
                stack.pop()
                stack.append(2 if temp_nums == [] else 2 * sum(temp_nums))
            elif stack[-1] == '[':
                answer = 0
                stack.clear()
                break
        elif s == ']':
            while stack and stack[-1] != '(' and stack[-1] != '[':
                temp_nums.append(stack.pop())

            if not stack:
                answer = 0
                stack.clear()
                break

            if stack[-1] == '[':
                stack.pop()
                stack.append(3 if temp_nums == [] else 3 * sum(temp_nums))
            elif stack[-1] == '(':
                answer = 0
                stack.clear()
                break
        else:
            stack.append(s)

if not stack:
    print(0)
elif '(' in set(stack) or '[' in set(stack):
    print(0)
else:
    print(sum(stack))
