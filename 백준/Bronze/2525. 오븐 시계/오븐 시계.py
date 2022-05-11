import sys

hh, mm = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().strip())

sec = ((hh * 60 + mm) * 60) 
new_sec = sec + c * 60


new_min = new_sec // 60
new_hh = new_min // 60
new_hh %= 24
new_mm = new_min % 60

print(new_hh, new_mm)

"""
00 00
23 59
86340초
시간은 무조건 초로 바꾸자!
"""
