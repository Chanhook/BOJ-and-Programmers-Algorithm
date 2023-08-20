s = input().strip()
t = input().strip()


def minus_a(string):
    return string[:-1]


def reverse_minus_b(string):
    return string[:-1][::-1]


for i in range(len(t) - len(s)):
    last_word = t[-1]
    if last_word == 'A':
        t = minus_a(t)
    else:
        t = reverse_minus_b(t)

print(1 if s == t else 0)