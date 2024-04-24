def solution(s):
    answer = []

    datas = to_data(s)

    visited = set()

    for data in datas:
        for d in data:
            if d not in visited:
                answer.append(int(d))
                visited.add(d)

    return answer


def to_data(s):
    ret = []
    s = s[2:-2].split("},{")

    for c in s:
        ret.append(c.split(','))

    ret.sort(key=lambda x: len(x))
    return ret