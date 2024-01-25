n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
cnt = 0

for start in range(n-1):
    end = start + 1
    while end < n and arr[start] + arr[end] < x:
        end += 1

    if end < n and arr[start] + arr[end] == x:
        cnt += 1

print(cnt)

