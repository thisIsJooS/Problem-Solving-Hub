# https://school.programmers.co.kr/learn/courses/30/lessons/135807

def solution(arrayA, arrayB):
    answer = max(f(arrayA, arrayB), f(arrayB, arrayA))

    return answer


def f(A, B):
    # A 는 다 나눠 떨어지고, B는 나누어지지 않는다

    tmp = A[0]
    for i in range(1, len(A)):
        tmp = g(tmp, A[i])

        if tmp == 1:  # 다 나눌 수 있는 것이 1이다
            return 0

    for i in range(len(B)):
        if B[i] % tmp == 0:
            return 0

    return tmp


def g(a, b):
    while b > 0:
        a, b = b, a % b

    return a