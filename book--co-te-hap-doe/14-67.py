# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(b, y):
    answer = []

    m = (b + 4 + (b ** 2 - 8 * b + 16 - 16 * y) ** (1 / 2)) // 4
    n = (b + 4) // 2 - m

    return [m, n]