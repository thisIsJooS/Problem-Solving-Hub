n, m = map(int, input().split())

q = [i for i in range(1, n+1)]

prev = 0
arr = []
while q:
    prev = (prev+(m-1))%n
    arr.append(q.pop(prev))

    n = len(q)


res = '<'
for a in arr:
    res += f'{a}, '

res = res[:-2]
res += '>'
print(res)