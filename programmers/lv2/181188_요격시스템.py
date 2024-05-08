# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    answer = 0

    targets.sort()
    start, end = targets[0]

    for t in targets[1:]:
        a, b = t

        if end <= a:
            answer += 1
            start, end = a, b
            continue

        start = a

        if b < end:
            end = b

    return answer + 1