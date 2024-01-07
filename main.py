arr = [[' '] * 15 for _ in range(5)]

for i in range(5):
    d = list(input())
    for j in range(len(d)):
        arr[i][j] = d[j]

s = ''
for j in range(15):
    for i in range(5):
        if arr[i][j] == ' ': continue
        s += arr[i][j]

print(s)
