# https://school.programmers.co.kr/learn/courses/30/lessons/169198


def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        a, b = ball
        ans1 = get1(startX, startY, a, b, n, m)
        ans2 = get1(startY, startX, b, a, m, n)
        # ans3 = get2(startX, startY, a, b, n, m)

        answer.append(min(ans1, ans2))

    return answer


def get1(x, y, a, b, n, m):
    if x == a:
        if b > y:
            return (y + b) ** 2
        else:
            return (2 * n - b - y) ** 2

    if b < y:
        x, y, a, b = a, b, x, y

    p = (a - x) / (b / y + 1)
    a1 = round(((p ** 2 + y ** 2) ** 0.5 + (b ** 2 * p ** 2 / y ** 2 + b ** 2) ** 0.5) ** 2)

    b = n - b
    y = n - y

    p = (a - x) / (b / y + 1)
    a2 = round(((p ** 2 + y ** 2) ** 0.5 + (b ** 2 * p ** 2 / y ** 2 + b ** 2) ** 0.5) ** 2)

    return min(a1, a2)


def get2(x, y, a, b, n, m):
    ans = 1e9

    if x < a and y < b:
        if y / x == b / a:
            ans = ((x ** 2 + y ** 2) ** 0.5 + (a ** 2 + b ** 2) ** 0.5) ** 2

    if x > a and y < b:
        a = m - a
        x = m - x
        if y / x == b / a:
            ans = ((x ** 2 + y ** 2) ** 0.5 + (a ** 2 + b ** 2) ** 0.5) ** 2

    if x < a and y > b:
        if (n - y) / x == (n - b) / a:
            ans = ((x ** 2 + (n - y) ** 2) ** 0.5 + (a ** 2 + (n - b) ** 2) ** 0.5) ** 2

    if x > a and y > b:
        if (x - a) / (y - b) == (m - a) / (n - b):
            ans = (((m - x) ** 2 + (n - y) ** 2) ** 0.5 + ((m - a) ** 2 + (n - b) ** 2) ** 0.5) ** 2

    return ans




