def count_bit_1(n):
    i = 1
    while True:
        if 5 ** i > n:
            if i > 1:
                a, b = divmod(n, 5 ** (i - 1))
                if a > 2:
                    cnt = count_bit_1(b)
                    return cnt + (4 ** (i - 1)) * (a - 1)
                elif a == 2:
                    return (4 ** (i - 1)) * 2
                else:
                    cnt = count_bit_1(b)
                    return cnt + (4 ** (i - 1)) * a
            else:
                if n >= 3:
                    return n - 1
                else:
                    return n
        elif 5 ** i == n: 
            return 4 ** i
        else:
            i += 1
            
def solution(n, l, r):
    answer = count_bit_1(r) - count_bit_1(l - 1)
    
    return answer