n, m = map(int, input().split())

res = []

start = 1
def f(num):
    if len(res) == m:
        print(*res)
        return

    for i in range(num, n+1):
        res.append(i)
        f(i)
        res.pop()


f(start)