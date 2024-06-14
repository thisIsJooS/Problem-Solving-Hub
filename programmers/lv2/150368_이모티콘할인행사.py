# https://school.programmers.co.kr/learn/courses/30/lessons/150368


def solution(users, emoticons):
    answer = [0, 0]

    def f(rate):
        nonlocal answer
        if len(rate) != len(emoticons):
            for n in [10, 20, 30, 40]:
                f(rate + [n])
            return

        total, register_cnt = 0, 0
        for user in users:
            r, c = user
            cost = 0
            for i in range(len(emoticons)):
                if rate[i] >= r:
                    cost += emoticons[i] * ((100 - rate[i]) / 100)

            if cost >= c:
                register_cnt += 1
            else:
                total += cost

        if answer[0] < register_cnt or (answer[0] == register_cnt and answer[1] < total):
            answer = [register_cnt, total]

    f([])

    return answer