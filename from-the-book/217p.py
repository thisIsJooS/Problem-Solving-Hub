"""
나누기 5
나누기 3
나누기 2
빼기 1
"""

n = int(input())

from collections import deque
arr = [987654321] * (n+1)
arr[n] = 0
q = deque([n])

while q:
    e = q.popleft()

    if e % 5 == 0:
        arr[e//5] = min(arr[e] + 1, arr[e//5])
        q.append(e//5)

    if e % 3 == 0:
        arr[e//3] = min(arr[e] + 1, arr[e//3])
        q.append(e//3)

    if e % 2 == 0:
        arr[e//2] = min(arr[e] + 1, arr[e//2])
        q.append(e//2)

    if 0 < e-1:
        arr[e-1] = min(arr[e] + 1, arr[e-1])
        q.append(e-1)


print(arr[1])


""" faster
x = int(input())

d = [0] * (x+1)

for i in range(2, x+1):
    d[i] = d[i-1] + 1

    if i%2 == 0 :
        d[i] = min(d[i], d[i//2]+1)

    if i%3 == 0 :
        d[i] = min(d[i], d[i//3]+1)

print(d[x])

"""