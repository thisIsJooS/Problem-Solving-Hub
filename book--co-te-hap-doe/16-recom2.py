# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 1

    routes.sort(key=lambda x: x[1], reverse=True)

    routes = list(map(f, routes))

    a, z = None, None
    for route in routes:
        l, r = route

        if a is None and z is None:
            a, z = l, r
            continue

        if a <= l <= z:
            if l > a:
                a = l
            if r < z:
                z = r
        else:
            answer += 1
            a, z = l, r

    return answer


def f(arr):
    return [-arr[1], -arr[0]]