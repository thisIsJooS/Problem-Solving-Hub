import copy

def rotate(key):
    n = len(key)
    res = [[None]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            res[i][j] = key[j][n-1-i]

    return res

def solution(key, lock):
    n, m = len(lock), len(key)

    total_board = [[0]*(2*m+n-2) for _ in range(2*m+n-2)]

    for i in range(m-1, m+n-1):
        for j in range(m-1, m+n-1):
            total_board[i][j] = lock[i-(m-1)][j-(m-1)]

    for i in range(m+n-1):
        for j in range(m+n-1):
            for _ in range(4):
                key = rotate(key)
                board = copy.deepcopy(total_board)
                for x in range(m):
                    for y in range(m):
                        board[i+x][j+y] += key[x][y]

                res = True
                for x in range(m-1, m+n-1):
                    if res:
                        for y in range(m-1, m+n-1):
                            if board[x][y] == 0 or board[x][y] == 2:
                                res = False
                                break
                    else:
                        break

                if res:
                    return True

    return False
