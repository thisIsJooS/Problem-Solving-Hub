import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

q = []
for i in range(n):
    q.append((a[i], i))
q.sort()

r = 0
p = [-1] * n
for e in q:
    _, i = e
    p[i] = r
    r += 1

print(*p)