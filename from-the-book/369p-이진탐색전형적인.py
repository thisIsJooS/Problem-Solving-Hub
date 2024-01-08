"""
공유기 설치
https://www.acmicpc.net/problem/2110
"""

import sys
input = sys.stdin.readline

n, c = list(map(int, input().split()))

arr = [int(input()) for _ in range(n)]
arr.sort()

start = 1
end = arr[-1] - arr[0]
res = 0

while start <= end:
    gap = (start + end) // 2
    prev = arr[0]
    count = 1

    for i in range(1, n):       # 앞에서부터 차근차근 설치
        if arr[i] >= prev + gap:
            prev = arr[i]
            count += 1

    if count >= c:  # c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = gap + 1
        res = gap
    else:
        end = gap - 1

print(res)
