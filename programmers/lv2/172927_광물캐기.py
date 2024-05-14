# https://school.programmers.co.kr/learn/courses/30/lessons/172927

def solution(picks, minerals):
    global answer
    answer = 1e9

    if len(minerals) > sum(picks) * 5:
        minerals = minerals[:sum(picks) * 5]

    n = len(minerals)

    maps = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    dic = {'diamond': 0, 'iron': 1, 'stone': 2}
    arr = []

    for i in range(0, n, 5):
        tmp = minerals[i:i + 5]
        e = []

        for p in range(3):
            val = 0
            for t in tmp:
                val += maps[p][dic[t]]

            e.append(val)

        arr.append(e)

    f(picks, arr, 0)

    return answer


def f(picks, arr, pirodo):
    global answer

    if not arr:
        answer = min(answer, pirodo)
        return

    if pirodo > answer:
        return

    for i in range(3):
        if picks[i] == 0:
            continue

        after_picks = picks[:]
        after_picks[i] -= 1
        f(after_picks, arr[1:], pirodo + arr[0][i])