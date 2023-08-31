def solution(new_id: str):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    temp_id = ''
    for s in new_id:
        if s in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            temp_id += s
    new_id = temp_id

    # 3단계
    temp_id = ''
    dot_cnt = 0
    for s in new_id:
        if s == '.':
            dot_cnt += 1
        else:
            if dot_cnt:
                temp_id += '.'
                dot_cnt = 0
            temp_id += s
    if dot_cnt:
        temp_id += '.'
    new_id = temp_id

    # 4단계
    if len(new_id) and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계
    if new_id == '':
        new_id += 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            last_word = new_id[-1]
            new_id += last_word

    return new_id
