def solution():
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = input().split()
        print(f(n, arr))

from itertools import combinations

def get_diff(a, b):
    ret = 0
    for i in range(4):
        if a[i] != b[i]:
            ret += 1

    return ret


def f(n, arr):
    answer = 1e9

    """
    나올 수 있는 종류의 수는 16가지이다. 
    n 이 17 이상이면, 적어도 두 쌍은 같은 것이 존재한다.
    n 이 33 이상이면, 적어도 세 쌍은 같은 것이 존재한다.
    
    feat. 비둘기집 원리
    """

    if n > 33:
        return 0

    for comb in combinations(arr, 3):
        a, b, c = comb
        dist = get_diff(a, b) + get_diff(b, c) + get_diff(a, c)

        answer = min(answer, dist)


    return answer

solution()