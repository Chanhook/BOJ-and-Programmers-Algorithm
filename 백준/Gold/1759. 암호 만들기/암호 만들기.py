import sys

input = sys.stdin.readline

l, c = map(int, input().split())
chars = list(input().split())
chars.sort()


def find(vow_cnt, con_cnt, string, index):
    if vow_cnt + con_cnt == l:
        if vow_cnt >= 1 and con_cnt >= 2:
            print(string)
        return

    for i in range(index, len(chars)):
        if chars[i] in ['a', 'e', 'i', 'o', 'u']:
            find(vow_cnt + 1, con_cnt, string + chars[i], i + 1)
        else:
            find(vow_cnt, con_cnt + 1, string + chars[i], i + 1)


find(0, 0, '', 0)
