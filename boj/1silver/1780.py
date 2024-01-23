import sys
input = sys.stdin.readline

def is_all_same(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j] != mat[0][0]:
                return None

    return mat[0][0]

def divide_9(mat):
    n = len(mat)
    if n == 1:
        return [mat]

    ret = []
    k = n // 3
    for x in range(0, n, k):
        for y in range(0, n, k):
            tmp = [[0] * k for _ in range(k)]
            for i in range(k):
                for j in range(k):
                    tmp[i][j] = mat[x+i][y+j]

            ret.append(tmp)
    return ret


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = [0, 0, 0]     # 0, 1, -1

def f(mat):
    is_same = is_all_same(mat)
    if is_same is not None:
        res[is_same] += 1
        return

    for divided in divide_9(mat):
        f(divided)


f(arr)
print(res[-1])
print(res[0])
print(res[1])