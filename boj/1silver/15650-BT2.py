n, m = map(int, input().split())

res = []

start = 0
def f(num):
    if len(res) == m:
        print(*res)
        return

    for i in range(num+1, n+1):
        if i not in res:
            res.append(i)
            f(i)
            res.pop()


f(start)