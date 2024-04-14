# https://school.programmers.co.kr/learn/courses/30/lessons/72411

# my
from itertools import combinations


def solution(orders, course):
    answer = []

    # 주문들을 일단 정렬
    for i, o in enumerate(orders):
        orders[i] = sorted(o)

    dict = {}
    for o in orders:
        length = len(o)
        for i in course:
            for comb in combinations(o, i):
                c = ''.join(sorted(comb))

                if c in dict:
                    dict[c] += 1
                else:
                    dict[c] = 1

    new_dict = {}
    for k, v in dict.items():
        if v >= 2:
            new_dict[k] = v

    dict = sorted(new_dict.items(), key=lambda x: (len(x[0]), -x[1]))
    print(dict)

    cur_length = len(dict[0][0])
    cur_val = dict[0][1]
    for k, v in dict:
        if cur_length == len(k):
            if v == cur_val:
                answer.append(k)

        else:
            cur_length = len(k)
            cur_val = v
            answer.append(k)

    return sorted(answer)


# book
from itertools import combinations
from collections import Counter


def _solution(orders, course):
    answer = []

    for c in course:  # 1. 각 코스 요리 길이에 대해
        menu = []

        for order in orders:  # 모든 주문에 대해
            comb = combinations(sorted(order), c)
            menu += comb

        counter = Counter(menu)  # 각 메뉴 구성이 몇번 주문되었는지 세어준다.

        if len(counter) != 0 and max(counter.values()) != 1:
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))

    return sorted(answer)