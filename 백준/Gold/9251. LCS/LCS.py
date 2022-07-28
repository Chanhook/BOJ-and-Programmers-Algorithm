str1 = input().strip()
str2 = input().strip()
l1 = len(str1)
l2 = len(str2)
lcs = [[0]*(l2+1) for _ in range(l1+1)]

for i in range(1, len(lcs)):
    for j in range(1, len(lcs[0])):
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[-1][-1])
