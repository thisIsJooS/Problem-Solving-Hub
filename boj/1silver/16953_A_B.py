"""
deque

2 -> 4, 21 -> 8, 41, 42, 211
만약 b 를 넘기면 하지마.

"""
from collections import deque

q = deque()
a, b = map(int, input().split())

q.append((a, 0))

while q:
    val, cnt = q.popleft()

    if val == b:
        print(cnt + 1)
        exit(0)

    if val*2 <= b:
        q.append((val*2, cnt+1))

    if int(str(val) + '1') <= b:
        q.append((int(str(val) + '1'), cnt+1))

print(-1)