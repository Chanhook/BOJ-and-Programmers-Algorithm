import sys
sys.setrecursionlimit(100000)

def solution(n, m, x, y, r, c, k):
    def dfs(cur_x, cur_y, cur_path, cur_k):
        if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m:
            return
        
        if flag[0] or abs(cur_x - (r-1)) + abs(cur_y - (c-1)) + cur_k > k:
            return
        
        if cur_k == k:
            if (cur_x, cur_y) == (r-1, c-1):
                flag[0] = True
                answer.append(''.join(cur_path)) 
            return 
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            cur_path.append(directions[i])
            cur_k += 1
            dfs(nx,ny,cur_path,cur_k)
            cur_path.pop()
            cur_k -= 1        
    
    diff = abs(x-r)+abs(y-c)
    if diff%2 != k%2 or diff > k:
        return 'impossible'
    
    answer = []
    flag = [False]
    
    
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    directions = ['d','l','r','u']
    
    dfs(x-1, y-1, [], 0)
    
    if answer:
        return answer[0]
    return 'impossible'