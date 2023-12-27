"""
https://www.acmicpc.net/problem/1793
2 X N 크기의 바닥에
1X2 , 2X1, 2X2
"""

import sys

dp = [0] * 251
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, 251):
    dp[i] = (dp[i - 2] * 2) + dp[i - 1]

while True:
    n = sys.stdin.readline().rstrip()

    if n.isdigit():
        print(dp[int(n)])
    else:
        break
