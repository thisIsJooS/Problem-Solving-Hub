# https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math
from collections import deque


def solution(progresses, speeds):
    answer = []

    q = deque()
    for i, _ in enumerate(progresses):
        q.append(math.ceil((100 - progresses[i]) / speeds[i]))

    while q:
        cnt = 1
        front = q.popleft()

        while q and q[0] <= front:
            q.popleft()
            cnt += 1

        answer.append(cnt)

    return answer