n = int(input().strip())
info = []
for i in range(n):
    name, kor, math, eng = input().split()
    info.append((name, int(kor), int(math), int(eng)))

sorted_info = sorted(info, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in sorted_info:
    print(i[0])
