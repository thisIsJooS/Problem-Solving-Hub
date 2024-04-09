# 요세푸스 문제

def solution(n, k):
    cur = 0

    arr = [i for i in range(1, n+1)]

    while len(arr) != 1:
        cur = (cur - 1 + k) % len(arr)

        arr.pop(cur)


    return arr[0]



print(solution(5, 2))

# ---------------------------
# https://www.acmicpc.net/problem/1158

from collections import deque

n, k = map(int, input().split())

q = deque(range(1, n+1))

answer = '<'
while q:
    for _ in range(k-1):
        q.append(q.popleft())

    answer += str(q.popleft())
    answer += ', '

print(answer[:-2] + '>')