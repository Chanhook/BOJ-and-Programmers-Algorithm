import copy

# def pprint(graph):
#     for row in graph:
#         print(*row)
#     print()

# sort 안하기 위해서 좌 우 상 하 순으로 dfs 진행 
dx = [-1 ,1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j, graph, position, n, num):    
    res = [position]
    
    for k in range(4):        
        nx, ny = i + dx[k], j + dy[k]
        
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
            graph[nx][ny] = 2
            res = res + dfs(nx, ny, graph, [position[0]+dx[k], position[1]+dy[k]], n, num)
        
    return res

def rotate(graph):
    n = len(graph)
    
    rotate_graph = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotate_graph[j][n-1-i] = graph[i][j]
    return rotate_graph
        
    
def solution(game_board, table):
    answer = 0
    n = len(game_board)    
    game_board_copy = copy.deepcopy(game_board)
    block = []
    
    for i in range(n):
        for j in range(n):
            if game_board_copy[i][j] == 0:
                game_board_copy[i][j] = 2
                result = dfs(i, j, game_board_copy, [0, 0], n, 0)[1:] # 처음 자기가 들어가니까
                # pprint(game_board_copy)
                block.append(result)
                # print(result)
                
    for r in range(4):
        table = rotate(table)
        table_rotate_copy = copy.deepcopy(table)
        
        for i in range(n):
            for j in range(n):
                if table_rotate_copy[i][j] == 1:
                    table_rotate_copy[i][j] = 2
                    result = dfs(i, j, table_rotate_copy, [0, 0], n, 1)[1:]
                    if result in block:
                        block.pop(block.index(result))
                        answer += (len(result)+1)                        
                        table = copy.deepcopy(table_rotate_copy)
                    else:
                        table_rotate_copy = copy.deepcopy(table)
    
    return answer