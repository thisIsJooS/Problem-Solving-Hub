def is_valid(string):
    if not is_balanced(string):
        return False

    t = 0
    for c in string:
        if c == '(':
            t += 1
        elif c == ')':
            if t == 0:
                return False
            t -= 1

    if t == 0:
        return True
    else:
        return False

def is_balanced(string):
    if not string:
        return False

    if string.count('(') == string.count(')'):
        return True
    return False


def converse(string):
    temp = ''
    for c in string:
        if c == '(':
            temp += ')'
        elif c == ')':
            temp += '('

    return temp


def solution(string):
    if not string:
        return string

    if is_valid(string):
        return string

    u, v = '', ''
    for i in range(2, len(string)+1):
        if is_balanced(string[:i]):
            u, v = string[:i], string[i:]   #2
            break


    if is_valid(u):     # 3
        return u + solution(v)

    # 4
    else:
        temp = '('          # 4-1
        temp += solution(v)        # 4-2
        temp += ')'         # 4-3
        temp += converse(u[1:-1])
        return temp


print(solution('))(('))