def solution(survey, choices):
    answer = ''
    
    character_list = ["R","T","C","F","J","M","A","N"]
    character_list2 = [["R","T"],["C","F"],["J","M"],["A","N"]]
    character = {c:0 for c in character_list}
    
    for qstn, ch in zip(survey, choices):
        if ch < 4:
            character[qstn[0]] += 4-ch
        elif ch > 4:
            character[qstn[1]] += ch-4
    
    for type1, type2 in character_list2:
        if character[type1] >= character[type2]:
            answer += type1
        else:
            answer += type2
        
    
    
    
    return answer