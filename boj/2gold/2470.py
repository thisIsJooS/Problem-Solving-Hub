"""
5
-2 4 -99 -1 98"""

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = [1e9, 1e9+1]

start = 0
end = n-1
while start < end:
    val = arr[start] + arr[end]

    if abs(val) < abs(sum(ans)):
        ans = [arr[start], arr[end]]

    if val > 0:
        end -= 1
    else:
        start += 1


ans.sort()
print(*ans)