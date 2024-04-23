# https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    s = list(str(n))
    s.sort(reverse=True)

    return int(''.join(s))