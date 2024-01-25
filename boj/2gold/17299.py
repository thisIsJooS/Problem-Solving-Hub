from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
stack = []
counter = Counter(arr)
res = [0] * n

for i in range(n-1, -1, -1):
    while stack and counter[arr[i]] >= stack[-1][1]:
        stack.pop()

    if stack:
        res[i] = stack[-1][0]
    else:
        res[i] = -1

    stack.append((arr[i], counter[arr[i]]))


print(*res)


"""
7
1 1 2 3 4 1 2
"""