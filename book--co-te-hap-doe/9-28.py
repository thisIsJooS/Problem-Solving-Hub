# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    answer = 1

    a = n - 1 + a
    b = n - 1 + b

    while parent(a) != parent(b):
        a = parent(a)
        b = parent(b)
        answer += 1

    return answer


def parent(i):
    return i // 2