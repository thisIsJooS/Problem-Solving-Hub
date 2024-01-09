import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cand = []
arr = []
for _ in range(n):
    cand.append(input())

for _ in range(m):
    arr.append(input())

cnt = 0
for a in arr:
    if a in cand:
        cnt += 1

print(cnt)