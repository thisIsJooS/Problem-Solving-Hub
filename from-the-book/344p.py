import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

distance = [int(1e9)] * (K+1)
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue

        val = board[i][j]
        dist = abs(i-X+1) + abs(j-Y+1)
        distance[val] = min(distance[val], dist)


if S < min(distance):
    print(0)
    exit(0)

print(distance.index(min(distance)))
