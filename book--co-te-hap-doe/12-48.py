"""
9x9 스도쿠 보드를 다 채워 완성된 스도쿠 보드를 반환하라
"""

def solution(board):
    def is_valid(num, row, col):
        return not(in_row(num , row) or in_col(num, col) or in_box(num, row, col))

    def in_row(num, row):
        return num in board[row]

    def in_col(num, col):
        return num in (board[i][col] for i in range(9))

    def in_box(num, row, col):
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row+3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return True
        return False

    def find_empty_position():
        # 스도쿠 보드에서 비어있는 위치 반환
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None


    def find_solution():
        empty_pos = find_empty_position()

        if not empty_pos:
            return True

        row, col = empty_pos
        for num in range(1, 10):
            if is_valid(num, row, col):
                board[row][col] = num
                if find_solution():
                    return True
            board[row][col] = 0

        return False

    find_solution()
    return board
