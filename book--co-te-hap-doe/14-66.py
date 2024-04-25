# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter


def solution(topping):
    answer = 0
    size = len(topping)

    counter = dict(Counter(topping))

    a = set()
    for i in range(size):
        e = topping[i]
        counter[e] -= 1

        if counter[e] == 0:
            del counter[e]

        a.add(e)

        if len(a) == len(counter):
            answer += 1

    return answer