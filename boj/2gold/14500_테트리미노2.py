# 나올 수 있는 블럭의 모양을 정의
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


# 왼쪽으로 90도 회전한 배열을 return
def rotate(arr):
    n, m = len(arr), len(arr[0])

    rotated = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            rotated[m-j-1][i] = arr[i][j]

    return rotated


# 매개변수로 주어진 block 영역의 최대합
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


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 입력 배열을 총 4번 회전시켜 모든 경우의 수를 계산함
for _ in range(4):
    for block in blocks:
        ret = get_max(block, maps)
        answer = max(answer, ret)
    maps = rotate(maps)

print(answer)