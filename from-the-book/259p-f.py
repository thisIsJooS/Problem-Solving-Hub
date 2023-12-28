# 플로이드-워셜 알고리즘 이용

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0


for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())    # 1-> K -> X

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


r = graph[1][k]
t = graph[k][x]

if r == INF or t == INF:
    print(-1)
else:
    print(r+t)


"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
>> 3

4 2
1 3
2 4
3 4
>> -1
"""