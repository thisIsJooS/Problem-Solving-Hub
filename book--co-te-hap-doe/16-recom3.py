# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack = []

    for n in number:
        if not stack:
            stack.append(n)
            continue

        while k > 0 and stack and n > stack[-1]:
            stack.pop()
            k -= 1

        stack.append(n)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
