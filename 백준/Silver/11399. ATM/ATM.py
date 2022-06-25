import sys

N = int(sys.stdin.readline().strip())
people = [x for x in list(map(int,sys.stdin.readline().split()))]
people.sort()

time = 0
for i in range(len(people)):
    time += sum(people[:i+1])

print(time)