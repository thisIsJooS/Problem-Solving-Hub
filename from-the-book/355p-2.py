from collections import deque

def solution(board):
    n = len(board[0])
    mat = []
    mat.append([1]*(n+2))
    for b in board:
        mat.append([1] + b + [1])
    mat.append([1]*(n+2))

    q = deque()
    start = {(1, 1), (1, 2)}
    q.append((start, 0))      # pos, dist
    visited = []
    visited.append(start)

    while q:
        now, dist = q.popleft()
        if (n, n) in now:
            return dist

        for pos in get_next(now, mat):
            if pos not in visited:
                visited.append(pos)
                q.append((pos, dist+1))


    return


def get_next(pos, mat):
    (x1, y1), (x2, y2) = sorted(pos)
    res = []

    # 가로일 경우
    if x1 == x2:
        for i in [-1, 1]:
            if mat[x1+i][y1] == 0 and mat[x1+i][y2] == 0:
                res.append({(x1+i, y1), (x1+i, y2)})
                res.append({(x1+i, y1), (x1, y1)})
                res.append({(x1+i, y2), (x1, y2)})
        if mat[x1][y1-1] == 0:
            res.append({(x1, y1-1), (x1, y1)})
        if mat[x1][y2+1] == 0:
            res.append({(x1, y2), (x1, y2+1)})



    elif y1 == y2:
        for i in [-1, 1]:
            if mat[x1][y1+i] == 0 and mat[x2][y1+i] == 0:
                res.append({(x1, y1+i), (x2, y1+i)})
                res.append({(x1, y1+i), (x1, y1)})
                res.append({(x2, y1+i), (x2, y1)})
        if mat[x1-1][y1] == 0:
            res.append({(x1-1, y1), (x1, y1)})
        if mat[x2+1][y1] == 0:
            res.append({(x2, y1), (x2+1, y1)})

    return res


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))