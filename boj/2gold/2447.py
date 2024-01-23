base = [['*']*3 for _ in range(3)]
base[1][1] = ' '

def x3(arr):
    ret = []
    length = len(arr)

    for i in range(length):
        tmp = arr[i]*3
        ret.append(tmp)

    for i in range(length):
        tmp = arr[i] + [' ']*length + arr[i]
        ret.append(tmp)

    for i in range(length):
        tmp = arr[i]*3
        ret.append(tmp)

    return ret


n = int(input())
k = 1

while 3**k < n:
    base = x3(base)
    k += 1

for b in base:
    for c in b:
        print(c, end='')
    print()