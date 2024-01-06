mat = [list(input()) for _ in range(8)]

res = 0
for i in range(0, 8, 2):
    for j in range(0, 8, 2):
        if mat[i][j] == 'F':
            res += 1

for i in range(1, 8, 2):
    for j in range(1, 8, 2):
        if mat[i][j] == 'F':
            res += 1

print(res)