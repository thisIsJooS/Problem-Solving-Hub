# https://school.programmers.co.kr/learn/courses/30/lessons/77486

# 통과
def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))

    total = {name: 0 for name in enroll}

    for i in range(len(seller)):
        money = amount[i] * 100
        cur_name = seller[i]

        while money > 0 and cur_name != "-":
            total[cur_name] += money - money // 10
            cur_name = parent[cur_name]
            money //= 10

    return [total[name] for name in enroll]


# 10/13 (시간 초과)
def _solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))

    total = {name:0 for name in enroll}

    for i, person in enumerate(seller):
        now = person
        profit = amount[i] * 100

        while now != '-':
            total[now] += (profit - profit // 10)
            now = parent[now]
            profit = profit // 10


    return [total[name] for name in enroll]
