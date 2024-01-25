import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    q.append(int(input()))

stack = []
res = []
for i in range(1, n+1):
    stack.append(i)
    res.append('+')

    while stack and q and stack[-1] == q[0]:
        stack.pop()
        q.popleft()
        res.append('-')

if stack or q:
    print('NO')
else:
    print(*res, sep='\n')