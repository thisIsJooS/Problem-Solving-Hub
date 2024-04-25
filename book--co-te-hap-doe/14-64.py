# 달팽이 수열

def solution(n):
    arr = [[0]*n for _ in range(n)]
    num = 1     # 시작 숫자

    start_row, end_row = 0, n-1
    start_col, end_col = 0, n-1

    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col, end_col+1):
            arr[start_row][i] = num
            num += 1
        start_row += 1

        for i in range(start_row, end_row+1):
            arr[i][end_col] = num
            num += 1
        end_col -= 1

        if start_row <= end_row:
            for i in range(end_col, start_col-1, -1):
                arr[end_row][i] = num
                num += 1
            end_row -= 1

        if start_col <= end_col:
            for i in range(end_row, start_row-1, -1):
                arr[i][start_col] = num
                num += 1
            start_col += 1

    return arr


print(*solution(4), sep='\n')
print(*solution(5), sep='\n')