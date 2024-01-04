from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = 1e9

    for start in range(length):
        for friends in permutations(dist, len(dist)):
            f = 1
            limit = weak[start] + friends[f-1]

            for i in range(start, start+length):
                if weak[i] > limit:
                    f += 1
                    if f > len(dist): break
                    limit = weak[i] + friends[f-1]

            answer = min(answer, f)

    if answer > len(dist):
        return -1

    return answer