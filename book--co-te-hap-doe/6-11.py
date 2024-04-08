# https://school.programmers.co.kr/learn/courses/30/lessons/12973?language=python3

def solution(s):
    answer = execute(s)

    return answer


def execute(s):
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        return 0

    return 1
