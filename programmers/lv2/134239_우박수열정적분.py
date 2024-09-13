# https://school.programmers.co.kr/learn/courses/30/lessons/134239?language=python3

areas = [0]


def solution(k, ranges):
    answer = []

    n = get_n(k)

    for r in ranges:
        answer.append(calculate(n, r))
    return answer


def calculate(n, _range):
    start, end = _range[0], _range[1]

    end = end + n

    # 시작점이 끝점보다 커서 유효하지 않다면 -1 로 정의한다.
    if start > end:
        return -1

    return areas[end] - areas[start]


# 1이 되는 n 을 구한다.
def get_n(pre, result=0):
    if pre == 1:
        return result

    if pre % 2 == 0:  # 짝수
        next = pre // 2
    else:
        next = pre * 3 + 1

    area = (pre + next) / 2
    areas.append(areas[-1] + area)

    return get_n(next, result + 1)
