def solution(rows, columns, queries):
    answer = []
    
    matrix = []
    for i in range(rows):
        row_list = [ i*columns + c for c in range(1,columns+1)]
        matrix.append(row_list)
    
    
    for query in queries:
        min_num = 100*100
        
        x1,y1,x2,y2 = query
        
        top = matrix[x1-1][y1-1:y2-1]
        min_num = min(min_num,min(top))
        
        bottom = matrix[x2-1][y1:y2]
        min_num = min(min_num,min(bottom))
        
        left = []
        for row in matrix[x1:x2]:
            left.append(row[y1-1])
        min_num = min(min_num,min(left))
        
        right = []
        for row in matrix[x1-1:x2-1]:
            right.append(row[y2-1])
        min_num = min(min_num,min(right))
        
        answer.append(min_num)
        
        for i in range(len(top)):
            matrix[x1-1][y1+i] = top[i]
            matrix[x2-1][y1-1+i] = bottom[i]
        
        for i in range(x2-x1):
            matrix[x1+i][y2-1] = right[i]
            matrix[x1-1+i][y1-1] = left[i]
            
        # print(matrix)
        
    return answer