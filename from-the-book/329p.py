def solution(n, build_frame):
    global x_board, y_board
    x_board = [[False] * (n+1) for _ in range(n+1)]
    y_board = [[False] * (n+1) for _ in range(n+1)]

    for bf in build_frame:
        x, y, a, b = bf
        if b == 1:      # 설치
            if a == 0 and valid_gidoong(x, y):
                y_board[x][y] = True
            elif a == 1 and valid_bo(x, y, n):
                x_board[x][y] = True

        else:           # 삭제
            if a == 1:
                x_board[x][y] = False

                if not is_valid_delete(n):
                    x_board[x][y] = True

            elif a == 0:
                y_board[x][y] = False

                if not is_valid_delete(n):
                    y_board[x][y] = True

    res = []
    for x in range(n+1):
        for y in range(n+1):
            if y_board[x][y]:
                res.append([x, y, 0])
            if x_board[x][y]:
                res.append([x, y, 1])

    return res


global x_board, y_board


def valid_gidoong(x, y):
    if y == 0:
        return True

    if x_board[x][y]:
        return True

    if x > 0 and x_board[x-1][y]:
        return True

    if y > 0 and y_board[x][y-1]:
        return True

    return False

def valid_bo(x, y, n):
    if y > 0 and y_board[x][y-1]:
        return True

    if y > 0 and x < n and y_board[x+1][y-1]:
        return True

    if 0 < x < n and x_board[x-1][y] and x_board[x+1][y]:
        return True

    return False


def is_valid_delete(n):
    for i in range(n+1):
        for j in range(n+1):
            if x_board[i][j] and not valid_bo(i, j, n):
                return False
            if y_board[i][j] and not valid_gidoong(i, j):
                return False

    return True


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))