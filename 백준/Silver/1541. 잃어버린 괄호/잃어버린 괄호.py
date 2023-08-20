equation = list(input().split('-'))


def calc(string):
    l = list(string.split('+'))
    return sum(int(num) for num in l)


result = calc(equation[0])
for i in range(1, len(equation)):
    result -= calc(equation[i])

print(result)
