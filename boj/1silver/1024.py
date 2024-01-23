N, L = map(int, input().split())

res = []
def f():
    for a in range(L, 101):
        for l in range(2, 101):
            if (2*N - a**2 + a) % (2*a) != 0:
                continue

            else:
                x = (2*N - a**2 + a) // (2*a)

                if x < 0:
                    continue

                for i in range(a):
                    res.append(x+i)

                return

f()
if res:
    print(*res)
else:
    print(-1)