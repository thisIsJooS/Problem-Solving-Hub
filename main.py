n, m = map(int, input().split())

arr = [0]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        arr[i] = c

print(*arr[1:])