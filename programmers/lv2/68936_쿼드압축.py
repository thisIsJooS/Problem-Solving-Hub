# https://school.programmers.co.kr/learn/courses/30/lessons/68936


def solution(arr):
    f(arr)

    return cnt


cnt = [0, 0]


def f(arr):
    if len(arr) == 1 or is_all_same(arr):
        cnt[arr[0][0]] += 1
        return

    for i in range(4):
        new_arr = get_new_arr(arr, i)
        if is_all_same(new_arr):
            cnt[new_arr[0][0]] += 1
        else:
            f(new_arr)


def is_all_same(arr):
    n = len(arr)
    num = arr[0][0]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != num:
                return False

    return True


def get_new_arr(arr, num):
    n = len(arr)
    half = n // 2

    tmp = []

    if num == 0:
        for i in range(half):
            tmp.append(arr[i][:half])
    elif num == 1:
        for i in range(half):
            tmp.append(arr[i][half:])
    elif num == 2:
        for i in range(half, n):
            tmp.append(arr[i][:half])
    else:
        for i in range(half, n):
            tmp.append(arr[i][half:])

    return tmp
