for _ in range(3):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    agg = sum(arr)
    if agg > 0:
        print('+')
    elif agg < 0:
        print('-')
    else:
        print('0')