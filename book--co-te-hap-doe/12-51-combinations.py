from itertools import combinations_with_replacement
from collections import Counter


def solution(n, info):
    answer = [-1]

    max_gap = 1

    for lion_comb in combinations_with_replacement(range(11), n):
        lion = comb_to_list(lion_comb)
        g = gap(lion, info)

        if g > max_gap:
            answer = lion[:]
            max_gap = g
        elif g == max_gap:
            answer = change(answer, lion[:])
            max_gap = g

    return answer


def comb_to_list(comb):
    arr = [0] * 11
    counter = Counter(comb)

    for k, v in counter.items():
        arr[k] = v

    return arr


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
    if len(old) == 1:
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
