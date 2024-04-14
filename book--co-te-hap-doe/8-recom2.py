def solution(msg):
    answer = []

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    dict = {}
    i = 1
    for alpha in alphabets:
        dict[alpha.upper()] = i
        i += 1

    ##
    idx = 0
    length = len(msg)

    while idx < length:
        cur = str(msg[idx])

        for i in range(1, length - idx):
            if cur + msg[idx + i] in dict:
                cur = cur + msg[idx + i]
            else:
                break

        answer.append(dict[cur])

        idx += len(cur)

        if idx < length:
            dict[cur + msg[idx]] = max(dict.values()) + 1

    return answer
