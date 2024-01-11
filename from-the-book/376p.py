n = int(input())
mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))

dx = [1, 1]
dy = [0, 1]

import copy
arr = copy.deepcopy(mat)

for x in range(n-1):
    for y in range(len(arr[x])):
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]

            arr[nx][ny] = max(arr[nx][ny], arr[x][y] + mat[nx][ny])


print(max(arr[n-1]))