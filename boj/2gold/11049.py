import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

dp = [[0] * n for _ in range(n)]

for size in range(1, n):
    for start in range(n-size):
        end = start + size

        val = 1e9
        for k in range(size):
            val = min(val, dp[start][start+k] + dp[start+k+1][end] + data[start][0] * data[start+k][1] * data[end][1])

        dp[start][end] = val

# print(*dp, sep='\n')
print(dp[0][n-1])



"""
4
5 4
4 3
3 2
2 1

38


4
5 3
3 2
2 6
6 3

96

5
1 10
10 1
1 10
10 1
1 10

31
"""