from itertools import combinations

t = int(input())

for _ in range(t):
    n = int(input())
    arr, ans = [], 1e13
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    for group1 in combinations(arr, n//2):
        group1 = list(group1)
        group2 = [e for e in arr if e not in group1]

        a, b = 0, 0
        for g in group1:
            a += g[0]
            b += g[1]

        for g in group2:
            a -= g[0]
            b -= g[1]

        ans = min(ans, a**2 + b**2)

    ans = pow(ans, 0.5)
    print(ans)
