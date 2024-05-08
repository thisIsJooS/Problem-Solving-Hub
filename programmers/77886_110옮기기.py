# https://school.programmers.co.kr/learn/courses/30/lessons/77886


def solution(s):
    answer = []

    for e in s:
        removed, cnt = devide(e)
        answer.append(get(removed, cnt))

    return answer


def get(s, cnt):
    idx = s.rfind('0') + 1

    if idx == -1:
        s = '110 ' *cnt + s
    else:
        s = s[:idx] + '110 ' *cnt + s[idx:]

    return s



def devide(s):
    stack = []
    cnt = 0

    for c in s:
        if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1' and c == '0':
            del stack[-1]
            del stack[-1]
            cnt += 1
        else:
            stack.append(c)


    return ''.join(stack), cnt
