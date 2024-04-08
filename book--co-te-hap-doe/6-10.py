# https://school.programmers.co.kr/learn/courses/30/lessons/76502?language=python3

from collections import deque

def solution(s):
    answer = 0

    s = deque(s)
    for _ in range(len(s)):
        if is_valid(s):
            answer += 1
        s = rotate(s)

    return answer


def rotate(q):
    q.append(q.popleft())

    return q


def is_valid(s):
    stack = []

    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif c == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()
        else:
            if not stack or stack[-1] != '[':
                return False
            stack.pop()

    if stack:
        return False

    return True