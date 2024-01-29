from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if a==b:
    print(0)
    print(1)
    exit(0)

visited = [0] * 100001

q= deque()
q.append((a, 0))
ans = 1e9
cnt = 0

while q:
    now, dist = q.popleft()
    visited[now] = 1

    if now-1 == b or now+1 == b or now*2 == b:
        if dist+1 < ans:
            ans = dist + 1
            cnt = 1
        elif dist+1 == ans:
            cnt +=1

    if now-1 >= 0 and not visited[now-1]:
        q.append((now-1, dist+1))
    if now+1 < 100001 and not visited[now+1]:
        q.append((now+1, dist+1))
    if now*2 < 100001 and not visited[now*2]:
        q.append((2*now, dist+1))


print(ans)
print(cnt)