n, b = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

def square_mat(arr):
    length = len(arr)
    ret = [[0]*length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            val = 0
            for k in range(length):
                val += (arr[i][k] * arr[k][j]) % 1000
            ret[i][j] = val % 1000

    return ret


def mult_arr(arr1, arr2):
    global n

    ret = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            val = 0
            for k in range(n):
                val += (arr1[i][k] * arr2[k][j]) % 1000
            ret[i][j] = val % 1000

    return ret


def f(arr, p):
    if p == 1:
        for i in range(len(arr)):
            for j in range(len(arr)):
                arr[i][j] %= 1000
        return arr

    if p % 2 == 0:
        return f(square_mat(arr), p//2)

    else:
        return mult_arr(arr, f(arr, p-1))

res = f(mat, b)

for r in res:
    print(*r)
