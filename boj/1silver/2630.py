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
    # 흰색이면 0, 파란색이면 1, 섞여있으면 -1

    color = arr[0][0]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != color:
                return -1

    return color

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]


res = [0, 0]
def f(arr):
    if len(arr) == 1:
        res[arr[0][0]] += 1
        return

    color = check(arr)
    if color != -1:
        res[color] += 1
        return

    d1, d2, d3, d4 = divide(arr)
    f(d1)
    f(d2)
    f(d3)
    f(d4)

f(mat)

print(*res, sep='\n')