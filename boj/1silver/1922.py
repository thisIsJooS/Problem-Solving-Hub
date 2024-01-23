def divide(arr):
    n = len(arr)
    d1, d2, d3, d4 = [], [], [], []

    mid = n // 2

    for i in range(mid):
        d1.append(arr[i][:mid])
        d2.append(arr[i][mid:])

    for i in range(mid, n):
        d3.append(arr[i][:mid])
        d4.append(arr[i][mid:])

    return d1, d2, d3, d4


def check(arr):
    n = len(arr)
    #  섞여있으면 -1

    color = arr[0][0]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != color:
                return -1

    return color


n = int(input())
mat = [list(map(int, list(input()))) for _ in range(n)]

s = ''
def f(arr, first, last):
    global s

    if first:
        s += '('


    if len(arr) == 1:
        s += str(arr[0][0])
        if last:
            s += ')'
        return

    color = check(arr)
    if color != -1:
        s += str(color)
        if last:
            s += ')'
        return

    d1, d2, d3, d4 = divide(arr)
    f(d1, True, False)
    f(d2, False, False)
    f(d3, False, False)
    f(d4, False, True)

    if last:
        s += ')'

f(mat, False, False)


print(s)
