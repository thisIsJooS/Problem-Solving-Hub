# https://school.programmers.co.kr/learn/courses/30/lessons/181187#

import math

def solution(r1, r2):
    frac = 0

    for a in range(1, r2 + 1):
        left = r1 ** 2 - a ** 2
        right = r2 ** 2 - a ** 2

        if left > 0:
            left = math.ceil(left ** 0.5)
            right = math.floor(right ** 0.5)

            frac += right - left + 1

        else:
            frac += 1 + math.floor(right ** 0.5)

    return 4 * frac