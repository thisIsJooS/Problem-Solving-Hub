N, M = map(int, input().split())
mat = [list(input()) for _ in range(N)]

res = int(1e9)
for i in range(0, N-7):
    for j in range(0, M-7):

        cnt = 0
        # 1. 흰색으로 시작할 경우
        for x in range(0, 8, 2):    # 흰
            for y in range(0, 8, 2):
                if mat[i+x][j+y] == 'B':
                    cnt += 1

        for x in range(1, 8, 2):    # 흰
            for y in range(1, 8, 2):
                if mat[i+x][j+y] == 'B':
                    cnt += 1

        for x in range(0, 8, 2):    # 검
            for y in range(1, 8, 2):
                if mat[i+x][j+y] == 'W':
                    cnt += 1

        for x in range(1, 8, 2):    # 검
            for y in range(0, 8, 2):
                if mat[i+x][j+y] == 'W':
                    cnt += 1

        res = min(res, cnt)

        cnt = 0
        # 2. 검으로 시작할 경우
        for x in range(0, 8, 2):  # 흰
            for y in range(0, 8, 2):
                if mat[i + x][j + y] == 'W':
                    cnt += 1

        for x in range(1, 8, 2):  # 흰
            for y in range(1, 8, 2):
                if mat[i + x][j + y] == 'W':
                    cnt += 1

        for x in range(0, 8, 2):  # 검
            for y in range(1, 8, 2):
                if mat[i + x][j + y] == 'B':
                    cnt += 1

        for x in range(1, 8, 2):  # 검
            for y in range(0, 8, 2):
                if mat[i + x][j + y] == 'B':
                    cnt += 1

        res = min(res, cnt)

print(res)
