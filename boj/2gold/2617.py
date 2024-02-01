import sys
input  = sys.stdin.readline

v, e = map(int, input().split())
graph = [[1e9] *(v+1) for _ in range(v+1)]

for _ in range(e):
    a, b= map(int, input().split())
    graph[b][a] = 1

for i in range(v+1):
    graph[i][i] = 0

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])



# for i in range(1, v+1):
#     for j in range(1, v+1):
#         if graph[i][j] == 1e9:
#             print('*', end=' ')
#         else:
#             print(graph[i][j], end=' ')
#
#     print()


def valid(a):
    if 0 < a < 1e9:
        return True

    return False

ans = 0
for i in range(1, v+1):
    cnt1 = 0
    cnt2 = 0
    for j in range(1, v+1):
        if valid(graph[i][j]):
            cnt1 += 1

        if valid(graph[j][i]):
            cnt2 += 1

    if cnt1 >= (v+1)//2:
        ans += 1
    elif cnt2 >= (v+1)//2:
        ans += 1

print(ans)

