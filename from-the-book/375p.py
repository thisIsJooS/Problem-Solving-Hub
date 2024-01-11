"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""

dx = [-1, 0, 1]
dy = [1, 1, 1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    line = list(map(int, input().split()))
    arr = []
    i = 0
    for _ in range(n):
        arr.append(line[i:i+m])
        i += m

    res = 0
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        tmp[i][0] = arr[i][0]

    for y in range(m):
        for x in range(n):
             for i in range(3):
                nx, ny = x + dx[i], y + dy[i]
                if not (0<=nx<n and 0<=ny<m) : continue

                if tmp[nx][ny] < tmp[x][y] + arr[nx][ny]:
                    tmp[nx][ny] = tmp[x][y] + arr[nx][ny]


    for x in range(n):
        res = max(res, tmp[x][m-1])


    print(res)