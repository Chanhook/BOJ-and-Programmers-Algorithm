def solution(number, k):
    stack = [number[0]]
    for n in number[1:]:
        while k > 0 and stack and int(stack[-1]) < int(n):
            stack.pop()
            k -= 1
        
        stack.append(n)
    
    l = len(number) - k
    return "".join(stack[:l])