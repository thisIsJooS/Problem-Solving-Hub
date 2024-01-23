n = int(input())

dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

now = 0
res = 0

while now < n-1:
    d = dist[now]


    for nex in range(now+1, n):
        if cost[now] <= cost[nex]:
            try:
                d += dist[nex]
            except:
                pass
        else:
            res += d * cost[now]
            now = nex
            break

        if nex == n-1:
            res += d * cost[now]
            now = nex


print(res)
