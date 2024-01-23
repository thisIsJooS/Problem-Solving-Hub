check = [True] * 1000001
check[0] = False
check[1] = False
prime = []

for i in range(2, 1000001):
    if check[i]:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = False


import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    cnt = 0

    for p in prime:
        if p >= n:
            break

        if check[n-p] and 2*p <= n:
            cnt += 1

    print(cnt)
