def rotate(arr):
    n = len(arr)
    m = len(arr[0])

    new_arr = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new_arr[m-j-1][i] = arr[i][j]

    return new_arr


def solution():
    n, m = map(int, input().split())

    maps = [list(map(int, input().split())) for _ in range(n)]

    blocks = [
        [[1, 1, 1, 1]],

        [[1, 1],
         [1, 1]],

        [[1, 0],
         [1, 0],
         [1, 1]],

        [[1, 0],
         [1, 1],
         [0, 1]],

        [[1, 1, 1],
         [0, 1, 0]],

        [[0, 1],
         [0, 1],
         [1, 1]],

        [[0, 1],
         [1, 1],
         [1, 0]],
    ]

    answer = 0
    for _ in range(4):
        for block in blocks:
            ret = get_max(block, maps)
            answer = max(answer, ret)
        maps = rotate(maps)

    return answer


def get_max(block, arr):
    N, M = len(arr), len(arr[0])
    n, m = len(block), len(block[0])

    ret = 0

    for i in range(N-n+1):
        for j in range(M-m+1):
            val = 0
            for x in range(i, i+n):
                for y in range(j, j+m):
                    val += block[x-i][y-j] * arr[x][y]

            ret = max(ret, val)

    return ret




print(solution())