from collections import defaultdict

def solution():
    n, m = map(int, input().split())
    dic = defaultdict()

    for _ in range(n):
        line = input()
        site, pw = line.split()
        dic[site] = pw

    wanna = [input() for _ in range(m)]

    for w in wanna:
        print(dic[w])

solution()