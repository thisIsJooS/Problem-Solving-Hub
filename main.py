import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    line = input().rstrip()

    sline = line.split()
    if len(sline) > 1:
        a, b = sline
        arr.append(b)

    else:
        c = sline[0]
        c = int(c)

        if c== 2:
            print(arr.pop() if arr else -1)
        elif c ==3:
            print(len(arr))
        elif c==4:
            print(0 if arr else 1)
        else:
            print(arr[-1] if arr else -1)