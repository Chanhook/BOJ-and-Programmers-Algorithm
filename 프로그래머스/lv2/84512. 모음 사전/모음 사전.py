from itertools import product

def solution(word):
    answer = 0
    
    dic = set()
    alp = ['','A','E','I','O','U']
    
    for pro in product(alp, alp, alp, alp, alp):
        dic.add(''.join(pro))
    
    dic = list(dic)
    dic.sort()
    answer = dic.index(word)
    
    return answer