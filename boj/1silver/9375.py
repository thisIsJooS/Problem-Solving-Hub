from collections import defaultdict

def f():
    dic = defaultdict(lambda: 0)
    n = int(input())

    for _ in range(n):
        line = input()
        a, b = line.split()
        dic[b] += 1

    ret = 1
    for v in dic.values():
        ret *= v+1


    return ret-1


T = int(input())

for _ in range(T):
    print(f())
