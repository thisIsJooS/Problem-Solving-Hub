# https://school.programmers.co.kr/learn/courses/30/lessons/92342#

def solution(n, info):
    answer = []
    max_gap = 1

    def dfs(lion_arr, k, prev):
        nonlocal answer, max_gap

        if k == n:
            g = gap(lion_arr, info)
            if g > max_gap:
                answer = lion_arr[:]
                max_gap = g
            elif g == max_gap:
                answer = change(answer, lion_arr[:])
                max_gap = g
            return

        for i in range(prev, 11):
            lion_arr[i] += 1
            dfs(lion_arr, k + 1, i)
            lion_arr[i] -= 1

    dfs([0] * 11, 0, 0)

    if answer:
        return answer
    else:
        return [-1]


def gap(lion, ap):
    l, a = 0, 0

    for i in range(11):
        if lion[i] == 0 and ap[i] == 0:
            continue
        elif lion[i] <= ap[i]:
            a += 10 - i
        else:
            l += 10 - i

    return l - a


def change(old, new):
    if not old:
        return new

    for i in range(10, -1, -1):
        if not old[i] and not new[i]:
            continue
        elif old[i] > new[i]:
            return old
        elif old[i] < new[i]:
            return new
        else:
            continue

    return old

