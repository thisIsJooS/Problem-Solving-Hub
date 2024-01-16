n = int(input())

res = []

def h(n, fro, to, mid):
    if n == 1:
        res.append((fro, to))
        return

    h(n-1, fro, mid, to)
    res.append((fro, to))
    h(n-1, mid, to, fro)

h(n, 1, 3, 2)

print(len(res))
for a, b in res:
    print(a, b)
