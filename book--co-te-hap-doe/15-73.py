# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0

    a, b = 0, 1

    for i in range(2, n + 1):
        answer = (a + b) % 1234567
        a = b
        b = answer % 1234567

    return answer