n, m = map(int, input().split())

res = []

def f():
    if len(res) == m:
        print(*res)
        return

    for i in range(1, n+1):
        res.append(i)
        f()
        res.pop()


f()