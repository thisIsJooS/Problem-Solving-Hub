# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(length, weight, truck_weights):
    time = 0
    middle, start = deque(), deque(truck_weights)

    while middle or start:
        time += 1

        if middle:
            pop_count = 0
            for _, t in middle:
                if time - t >= length:
                    pop_count += 1
                else:
                    break

            for _ in range(pop_count):
                middle.popleft()

        if start and _sum(middle) + start[0] <= weight:
            middle.append((start.popleft(), time))

    return time


def _sum(q):
    agg = 0
    for w, _ in q:
        agg += w

    return agg