n = int(input().strip())
info = [input().split() for _ in range(n)]

sorted_info = sorted(info, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in sorted_info:
    print(student[0])
