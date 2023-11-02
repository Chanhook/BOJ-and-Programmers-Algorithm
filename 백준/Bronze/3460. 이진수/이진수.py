def find_one(n):
    bit = []

    while n:
        bit.append(n % 2)
        n //= 2

    result = []
    for i in range(len(bit)):
        if bit[i] == 1:
            result.append(i)

    return result


T = int(input())
for t in range(T):
    n = int(input())
    result = find_one(n)
    print(*result)
