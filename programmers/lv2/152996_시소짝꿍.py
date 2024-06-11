# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import Counter


def solution(weights):
    answer = 0

    counter = Counter(weights)
    for key, val in counter.items():
        answer += val * (val - 1)

        answer += counter[(2 / 3) * key] * val
        answer += counter[(1 / 2) * key] * val
        answer += counter[(3 / 2) * key] * val
        answer += counter[(3 / 4) * key] * val
        answer += counter[(2) * key] * val
        answer += counter[(4 / 3) * key] * val

    return answer // 2