# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    answer = 0
    arr = [0] * 60001

    arr[1] = 1
    arr[2] = 2

    for i in range(3, n + 1):
        arr[i] = (arr[i - 1] + arr[i - 2]) % 1_000_000_007

    return arr[n]