from itertools import combinations

N = int(input())
mat = []
empties = []
teachers = []
for i in range(N):
    mat.append(list(input().split()))

    for j in range(N):
        if mat[i][j] == 'X':
            empties.append((i, j))
        elif mat[i][j] == 'T':
            teachers.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

found = False
for perm in combinations(empties, 3):
    possible = True

    for x, y in perm:
        mat[x][y] = 'O'

    for x, y in teachers:
        for i in range(4):
            nx, ny = x, y
            while 0<=nx<N and 0<=ny<N:
                nx, ny = nx + dx[i], ny + dy[i]
                if not (0<=nx<N and 0<=ny<N): continue

                if mat[nx][ny] == 'S':       # 학생 만남
                    possible = False    # 이 조합은 망함
                    break
                elif mat[nx][ny] == 'O':
                    break

            if not possible: break
        if not possible: break

    if possible:
        print('YES')
        exit(0)

    for x, y in perm:
        mat[x][y] = 'X'

print('NO')




