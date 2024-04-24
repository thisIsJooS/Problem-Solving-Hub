# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []

    datas = string_to_set(s)
    visited = set()

    for data in datas:
        for d in data:
            if d not in visited:
                answer.append(d)
                visited.add(d)

    return answer


def string_to_set(s):
    ret = []
    stack = []

    for c in s:
        if c == '}':
            num = ''
            tmp = set()
            while stack:
                if stack[-1].isdigit():
                    num += stack.pop()
                elif stack[-1] == ',':
                    stack.pop()
                    if num:
                        tmp.add(int(num[::-1]))
                        num = ''
                elif stack[-1] == '{':
                    if num:
                        tmp.add(int(num[::-1]))
                        num = ''
                    break

            if tmp: ret.append(tmp)


        else:
            stack.append(c)

    ret.sort(key=lambda x: len(x))

    return ret