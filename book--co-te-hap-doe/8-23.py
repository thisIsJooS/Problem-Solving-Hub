# https://school.programmers.co.kr/learn/courses/30/lessons/42579

# my
def solution(genres, plays):
    answer = []

    g_dic = {}
    for i, g in enumerate(genres):
        if g not in g_dic:
            g_dic[g] = [plays[i], [(i, plays[i])]]
        else:
            g_dic[g][0] += plays[i]
            g_dic[g][1].append((i, plays[i]))

    arr = sorted(g_dic.items(), key=lambda item: -item[1][0])
    for a in arr:
        li = a[1][1]
        li.sort(key=lambda x: x[1], reverse=True)

        answer.extend([i[0] for i in li[:2]])

    return answer
