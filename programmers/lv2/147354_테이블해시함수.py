# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    answer = []

    data.sort(key=lambda x: (x[col - 1], -x[0]))

    for i in range(row_begin - 1, row_end):
        s = 0
        for d in data[i]:
            s += d % (i + 1)

        answer.append(s)

    ret = None
    for i, a in enumerate(answer):
        if i == 0:
            ret = a
            continue

        ret = ret ^ a

    return ret