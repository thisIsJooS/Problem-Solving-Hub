a = ' ' + input()
b = ' ' + input()

maps = [[0] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            maps[i][j] = maps[i-1][j-1] + 1

res = max(map(max, maps))

print(res)