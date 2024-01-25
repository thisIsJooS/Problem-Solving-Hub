n = int(input())
arr = list(map(int, input().split()))

stack = [arr[-1]]
res = [-1 for _ in range(n)]
for i in range(n-2, -1, -1):
    while stack and arr[i] >= stack[-1]:
        stack.pop()

    if stack:
        res[i] = stack[-1]
    else:
        res[i] = -1

    stack.append(arr[i])

print(*res)