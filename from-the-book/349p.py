N = int(input())
arr = list(map(int, input().split()))
plus, minus, mult, div = map(int, input().split())

op = []
for _ in range(plus):
    op.append(0)
for _ in range(minus):
    op.append(1)
for _ in range(mult):
    op.append(2)
for _ in range(div):
    op.append(3)


from itertools import permutations

max_val = -int(1e9); min_val = int(1e9)
for perm in permutations(op, len(op)):
    t = arr[0]
    for i in range(N-1):
        if perm[i] == 0:
            t += arr[i+1]
        elif perm[i] == 1:
            t -= arr[i+1]
        elif perm[i] == 2:
            t *= arr[i+1]
        else:
            if t < 0:
                t = -t
                t //= arr[i+1]
                t = -t
            else:
                t //= arr[i+1]

    max_val = max(max_val, t)
    min_val = min(min_val, t)

print(max_val)
print(min_val)
