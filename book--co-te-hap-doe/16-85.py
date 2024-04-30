# https://school.programmers.co.kr/learn/courses/30/lessons/12979

import math


def solution(n, stations, w):
    answer = 0

    now = 1
    arr = []
    for s in stations:
        arr.append(s - w - now)
        now = s + w + 1

    if n + 1 - now >= 1:
        arr.append(n + 1 - now)

    for a in arr:
        answer += math.ceil(a / (2 * w + 1))

    return answer


def _solution(n, stations, w):
    answer = 0

    location = 1
    idx = 0

    while location <= n:
        if idx < len(stations) and location >= stations[idx] - w:
            location = stations[idx] + w + 1
            idx += 1
        else:
            location += 2 * w + 1
            answer += 1

    return answer


