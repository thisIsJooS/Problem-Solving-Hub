# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    answer = 1

    counter = Counter(tangerine)

    arr = sorted(counter.values(), reverse=True)

    total = 0
    for a in arr:
        if total + a < k:
            answer += 1
            total += a
        else:
            break

    return answer