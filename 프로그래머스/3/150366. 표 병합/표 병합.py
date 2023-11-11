def find(parent, x, y):
    p_ = parent[x][y]
    if (x, y) != p_:
        nx, ny = p_
        p_ = find(parent, nx, ny)
    return p_


def union(parent, x1, y1, x2, y2):
    pr1, pc1 = find(parent, x1, y1)
    pr2, pc2 = find(parent, x2, y2)

    parent[x2][y2] = (pr1, pc1)

    return


def solution(commands):
    answer = []

    n = 50
    EMPTY = 'EMPTY'
    loc = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    parent = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            parent[i][j] = (i, j)
            loc[i][j] = EMPTY

    for command in commands:
        c = command.split()
        if c[0] == 'UPDATE':
            if len(c) == 3:
                value, new_value = c[1:]
                for i in range(1, n + 1):
                    for j in range(1, n + 1):
                        if loc[i][j] == value:
                            loc[i][j] = new_value
            else:
                r, c, value = c[1:]
                r, c = int(r), int(c)
                pr, pc = find(parent, r, c)
                loc[pr][pc] = value
        elif c[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, c[1:])
            find1 = find(parent, r1, c1)
            find2 = find(parent, r2, c2)
            if find1 == find2:
                continue

            if loc[find1[0]][find1[1]] != EMPTY and loc[find2[0]][find2[1]] == EMPTY:
                for i in range(1, n + 1):
                    for j in range(1, n + 1):
                        if find2 == parent[i][j]:
                            union(parent, r1, c1, i, j)
            elif loc[find2[0]][find2[1]] != EMPTY and loc[find1[0]][find1[1]] == EMPTY:
                for i in range(1, n + 1):
                    for j in range(1, n + 1):
                        if find1 == parent[i][j]:
                            union(parent, r2, c2, i, j)
            elif loc[find1[0]][find1[1]] != EMPTY and loc[find2[0]][find2[1]] != EMPTY:
                for i in range(1, n + 1):
                    for j in range(1, n + 1):
                        if find2 == parent[i][j]:
                            union(parent, r1, c1, i, j)
            elif loc[find1[0]][find1[1]] == EMPTY and loc[find2[0]][find2[1]] == EMPTY:
                if (r1, c1) <= (r2, c2):
                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            if find2 == parent[i][j]:
                                union(parent, r1, c1, i, j)
                else:
                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            if find1 == parent[i][j]:
                                union(parent, r2, c2, i, j)
        elif c[0] == 'UNMERGE':
            r, c = map(int, c[1:])
            result = find(parent, r, c)
            value = loc[result[0]][result[1]]
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if result == find(parent, i, j):
                        parent[i][j] = (i, j)
                        loc[i][j] = EMPTY
            loc[r][c] = value
        elif c[0] == 'PRINT':
            r, c = int(c[1]), int(c[2])
            pr, pc = find(parent, r, c)
            answer.append(loc[pr][pc])

    return answer