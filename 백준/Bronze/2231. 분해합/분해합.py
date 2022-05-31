divsum_dic=dict()

for num in range(1,1000001):
    divsum = num + sum([int(s) for s in str(num)])
    if divsum not in divsum_dic:
        divsum_dic[divsum]=num
    else:
        divsum_dic[divsum]=min(divsum_dic[divsum],num)

n = int(input())

if n in divsum_dic:
    print(divsum_dic[n])
else:
    print(0)
