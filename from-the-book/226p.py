"""
최소한의 화폐 개수
"""

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

# arr 에 담긴 화폐 단위들로, 최소로 m을 구성하라.      2와 3으로 15를
# 가능하면 몇번? 불가능하면 -1

dp = [10001] * 10001

for a in arr:
    dp[a] = 1

# 0 1 1 2 2 2 3 3 3 5
for i in range(m+1):
    for a in arr:
        if i > a:
            dp[i] = min(dp[i], dp[i-a]+1)


print(dp[m]) if dp[m] <= 100 else print(-1)


"""
2 15 
2
3
--5

3 4 
3
5
7
-- -1

"""