# https://school.programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    arr = []
    for file in files:
        head, number, tail = do_split(file)
        arr.append([head, number, tail])

    arr.sort(key=lambda x: (x[0].lower(), int(x[1])))

    return [''.join(a) for a in arr]


def do_split(s):
    head, number, tail = '', '', ''

    for i in range(len(s)):
        if s[i].isdigit():
            head = s[:i]
            number = s[i:]
            break

    for i in range(len(number)):
        if not number[i].isdigit():
            tail = number[i:]
            number = number[:i]
            break

    return head, number, tail


