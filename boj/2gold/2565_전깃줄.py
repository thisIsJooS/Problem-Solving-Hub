arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr = [a[1] for a in sorted(arr)]

"""
arr : [8, 2, 9, 1, 4, 6, 7, 10]
최소한의 값을 제거하여 증가하는 부분 수열로 만들어라
-> (배열 길이) - (가장 긴 증가하는 부분 수열의 길이)
"""

dp = [1] * len(arr)
for i in range(len(arr)):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

print(len(arr) - max(dp))