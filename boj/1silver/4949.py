while True:
    line = input()
    if line == '.': exit(0)

    a, b = 0, 0
    res = True
    q = []
    for c in line:
        if c not in ['(', ')', '[', ']']:
            continue

        if c == '(':
            q.append(c)

        elif c == '[':
            q.append(c)

        elif c == ')':
            if not q or q[-1] != '(':
               res = False
               break

            q.pop()

        elif c == ']':
            if not q or q[-1] != '[':
                res = False
                break
            q.pop()

    if q: res = False

    print('yes' if res else 'no')
