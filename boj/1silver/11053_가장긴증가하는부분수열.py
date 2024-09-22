n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    tmp = 0                             # arr[i] 보다 왼쪽에 위치하면서 값이 작은 얘들 중 최대값을 찾기 위해 선언한 임시 변수
    for j in range(i-1, -1, -1):        # 현재 위치에서 왼쪽 방향으로 dp 테아블을 훑어간다.
        if arr[j] < arr[i]:             # 현재 나보다 작은 얘들 중에서 dp 값 중 최대값을 찾는다.
            if dp[j] > tmp:
                tmp = max(tmp, dp[j])

    dp[i] = tmp + 1

print(max(dp))

