def L(x, y):
    if x == -5:
        return None

    return x - 1, y


def R(x, y):
    if x == 5:
        return None

    return x + 1, y


def U(x, y):
    if y == 5:
        return None

    return x, y + 1


def D(x, y):
    if y == -5:
        return None

    return x, y - 1


def solution(dirs):
    answer = 0
    visited = set()

    x = y = 0

    for d in dirs:
        ret = 0, 0

        if d == 'U':
            ret = U(x, y)
        elif d == 'D':
            ret = D(x, y)
        elif d == 'R':
            ret = R(x, y)
        else:
            ret = L(x, y)

        if ret is None:
            continue

        nx, ny = ret
        path = tuple(sorted([(x, y), (nx, ny)]))
        if path not in visited:
            visited.add(path)
            answer += 1

        x, y = nx, ny

    return answer
