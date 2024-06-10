# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def solution(x, y, n):
    answer = -1

    dp = [1e9] * 1_000_001
    dp[x] = 0
    q = deque()
    q.append(x)

    while q:
        now = q.popleft()

        if now == y:
            answer = dp[y]
            break

        dist = dp[now] + 1

        if now + n <= y and dist < dp[now + n]:
            dp[now + n] = dist
            q.append(now + n)
        if now * 2 <= y and dist < dp[now * 2]:
            dp[now * 2] = dist
            q.append(now * 2)
        if now * 3 <= y and dist < dp[now * 3]:
            dp[now * 3] = dist
            q.append(now * 3)

    return answer