# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0

    d.sort()

    for e in d:
        budget -= e

        if budget < 0:
            break

        answer += 1

    return answer