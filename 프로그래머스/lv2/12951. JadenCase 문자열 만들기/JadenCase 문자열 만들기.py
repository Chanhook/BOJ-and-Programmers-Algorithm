def solution(s):
    answer = ''
    is_first = True
    for word in s:
        if is_first and word != " ":
            answer += word.upper()
            is_first = False
        else:
            if word == " ":
                is_first = True
                answer += word
            else:
                answer += word.lower()
    
    return answer