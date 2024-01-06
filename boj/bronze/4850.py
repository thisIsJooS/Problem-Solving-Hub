import sys

lines = sys.stdin.readlines()

for line in lines:
    n, w, d, result = map(int, line.split())

    v = (w*n*(n-1)//2 - result)

    if v == 0:
        print(n)
        continue

    res =  v // d
    print(res)