"""
이거 맞긴 맞거등여?
근데 dfs 로 풀어가지고 시간 오래걸린다고 테스트4부터 시간초과라고 실패 날려버림
마지막엔 재귀 깊이 초과로 그냥 런타임엘ㄹ뤠뤫ㅈ붸붸붸붸부베ㅞ부베ㅜ베굽국베굽겝ㄱ

그냥 곱게 BFS로 풀자 에효
"""


def solution(board):
    f(0, 0, 0, 1, set(), 0, len(board[0]), board)
    return res

def f(x1, y1, x2, y2, visited, count, n, board):
    global res, functions

    if x2 == (n-1) and y2 == (n-1):
        res = min(count, res)
        return

    visited.add((x1, y1, x2, y2))

    for func in functions:
        coord = func(x1, y1, x2, y2, n, board)
        if coord is not None and coord not in visited:
            f(*coord, set(visited), count + 1, n, board)

    return


def move_1(x1, y1, x2, y2, n, board):
    if x1 == x2:    # -- 가로 방향일 경우
        if x1 == 0 or board[x2-1][y2] or board[x1-1][y1]:
            return None
        return x1-1, y1, x2, y1
    # | 세로 방향일 경우
    else:
        if y1 == n-1 or board[x1][y1+1] or board[x2][y2+1]:
            return None
        return x1, y1, x1, y2+1

def move_2(x1, y1, x2, y2, n, board):
    if x1 == x2:    # -- 가로 방향일 경우
        if y1 == 0 or board[x1][y1-1]:
            return None
        return x1, y1-1, x2, y2-1

    # | 세로 방향일 경우
    else:
        if x1 == 0 or board[x1-1][y1]:
            return None
        return x1-1, y1, x1, y2


def move_3(x1, y1, x2, y2, n, board):
    if x1 == x2:    # -- 가로 방향일 경우
        if x1 == n-1 or board[x1+1][y2] or board[x1+1][y1]:
            return None
        return x1, y1, x2+1, y1
    # | 세로 방향일 경우
    else:
        if y1 == 0 or board[x1][y1-1] or board[x2][y2-1]:
            return None
        return x1, y1-1, x1, y1

def move_4(x1, y1, x2, y2, n, board):
    if x1 == x2:    # -- 가로 방향일 경우
        if x1 == 0 or board[x1 - 1][y1] or board[x2 - 1][y2]:
            return None
        return x1 - 1, y1, x2 - 1, y2
    # | 세로 방향일 경우
    else:
        if y1 == n-1 or board[x1][y1+1] or board[x2][y2+1]:
            return None
        return x1, y1+1, x2, y2+1

def move_5(x1, y1, x2, y2, n, board):
    if x1 == x2:    # -- 가로 방향일 경우
        if x1 == n - 1 or board[x1 + 1][y1] or board[x2 + 1][y2]:
            return None
        return x1 + 1, y1, x2 + 1, y2
    # | 세로 방향일 경우
    else:
        if y1 == 0 or board[x1][y1-1] or board[x2][y2-1]:
            return None
        return x1, y1-1, x2, y2-1

def move_6(x1, y1, x2, y2, n, board):
    if x1 == x2:    # -- 가로 방향일 경우
        if x1 == 0 or board[x2 - 1][y2] or board[x1 - 1][y1]:
            return None
        return x1-1, y2, x2, y2
    # | 세로 방향일 경우
    else:
        if y1 == n-1 or board[x1][y1+1] or board[x2][y2+1]:
            return None
        return x2, y2, x2, y2+1

def move_7(x1, y1, x2, y2, n, board):
    if x1 == x2:    # -- 가로 방향일 경우
        if y2 == n-1 or board[x1][y2 + 1]:
            return None
        return x2, y2, x2, y2+1

    # | 세로 방향일 경우
    else:
        if x2 == n-1 or board[x2+1][y2]:
            return None
        return x2, y2, x2+1, y2


def move_8(x1, y1, x2, y2, n, board):
    if x1 == x2:    # -- 가로 방향일 경우
        if x1 == n - 1 or board[x1 + 1][y2] or board[x1 + 1][y1]:
            return None
        return x2, y2, x2+1, y2
    # | 세로 방향일 경우
    else:
        if y1 == 0 or board[x1][y1 - 1] or board[x2][y2 - 1]:
            return None
        return x2, y2-1, x2, y2



res = int(1e9)
functions = [move_1, move_2, move_3, move_4, move_5, move_6, move_7, move_8]


