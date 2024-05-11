def solution():
    n, m = map(int, input().split())
    maps = [list(map(int, list(input()))) for _ in range(n)]

    maxp = min(n, m)

    for p in range(maxp-1, -1, -1):
        for i in range(n):
            for j in range(m):
                if i+p >= n or j+p >=m: continue

                val = maps[i][j]

                if maps[i+p][j] == val and maps[i][j+p] == val and maps[i+p][j+p] == val:
                    return (p+1) ** 2


print(solution())