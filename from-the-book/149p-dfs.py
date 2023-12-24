n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

res = 0
def dfs(x, y):
    if not (0<=x<n and 0<=y<m):     # 범위 벗어나면 땡
        return False

    if board[x][y] != 0:            # 방문했거나 못가면 땡
        return False

    board[x][y] = 2                 # 방문 처리

    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)

    return True


for x in range(n):
    for y in range(m):
        if dfs(x, y):
            res += 1

print(res)


""" inputs
4 5
00110
00011
11111
00000
"""#3

"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""#8