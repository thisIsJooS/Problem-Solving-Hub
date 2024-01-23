def check_row(x, a):
    for i in range(9):
        if a == mat[x][i]:
            return False
    return True


def check_col(x, a):
    for i in range(9):
        if a == mat[i][x]:
            return False
    return True


def check_box(x, y, a):
    x, y = x//3*3, y//3*3

    for i in range(3):
        for j in range(3):
            if a == mat[x+i][y+j]:
                return False
    return True


def f(num):
    if num == len(blank):
        for m in mat:
            print(*m)
        exit(0)

    for i in range(1, 10):
        x, y = blank[num]

        if check_row(x, i) and check_col(y, i) and check_box(x, y, i):
            mat[x][y] = i
            f(num+1)
            mat[x][y] = 0


mat = []
blank = []
for _ in range(9):
    line = list(map(int, input().split()))

    for i in range(9):
        if not line[i]:
            blank.append((_, i))

    mat.append(line)

f(0)



