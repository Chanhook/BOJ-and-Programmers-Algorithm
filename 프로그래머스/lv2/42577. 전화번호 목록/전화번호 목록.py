def solution(phone_book):
    # 정렬
    phone_book.sort(key=len)
    hash_table = {}

    # 맨 처음 가장 짧은 길이를 저장. min.
    min_len = len(phone_book[0])

    for target in phone_book:
        # loop마다 본인 정보를 hash table에 저장.
        hash_table[hash(target)] = target
        for i in range(min_len,len(target)):
            try:
                if hash_table[hash(target[:i])]:
                    return False
            except KeyError:
                continue
    return True