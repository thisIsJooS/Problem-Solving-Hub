# https://school.programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    n = len(board)
    m = len(board[0])

    for i in range(1, n):
        for j in range(1, m):
            if not board[i][j]:
                continue

            val = min(board[i][j - 1], board[i - 1][j - 1], board[i - 1][j])
            board[i][j] = val + 1

    answer = max(map(max, board))

    return answer ** 2