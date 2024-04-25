# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = []
    a, b = 0, 0

    while s != '1':
        b += s.count('0')
        s = f(s)
        a += 1

    return [a, b]


def f(s):
    s = s.replace('0', '')

    return toB(len(s))


def toB(n):
    stack = []

    while n != 0:
        stack.append(str(n % 2))
        n //= 2

    return ''.join(stack[::-1])