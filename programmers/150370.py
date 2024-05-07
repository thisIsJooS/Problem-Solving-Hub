# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []

    terms = get_terms_dict(terms)

    for i, p in enumerate(privacies):
        date, type = p.split()
        year, month, day = map(int, date.split('.'))

        limit_date = get_limit_date(year, month, day, terms[type])

        compared = compare_date(today, f'{limit_date[0]}.{limit_date[1]}.{limit_date[2]}')
        if compared == 1:
            answer.append(i + 1)

    return answer


def compare_date(now, date):
    now = list(map(int, now.split('.')))
    date = list(map(int, date.split('.')))

    if now[0] > date[0]:
        return 1
    elif now[0] < date[0]:
        return -1
    else:
        if now[1] > date[1]:
            return 1
        elif now[1] < date[1]:
            return -1
        else:
            if now[2] >= date[2]:
                return 1
            elif now[2] < date[2]:
                return -1


def get_limit_date(year, month, day, limit):
    month += limit
    while month > 12:
        year += 1
        month -= 12

    return year, month, day


def get_terms_dict(terms):
    d = {}

    for t in terms:
        a, b = t.split()
        d[a] = int(b)

    return d