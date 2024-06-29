# 0은 빈 칸, 1은 집, 2는 치킨집

from itertools import combinations

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

chicken_houses = []
houses = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chicken_houses.append((i, j))
        elif maps[i][j] == 1:
            houses.append((i, j))

answer = 1e9

for comb in combinations(chicken_houses, m):
    val = 0

    for h in houses:
        hx, hy = h

        dist = 1e9
        for com in comb:
            cx, cy = com

            d = abs(hx-cx) + abs(hy-cy)
            dist = min(dist, d)

        val += dist

    answer = min(answer, val)


print(answer)

