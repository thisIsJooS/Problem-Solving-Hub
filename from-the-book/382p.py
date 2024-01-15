string = []
string.append(input())
string.append(input())

n = len(string[0])
m = len(string[1])

arr = [[0] * n for _ in range(m)]

for i in range(n):
    arr[0][i] = i

for i in range(m):
    arr[i][0] = i


for i in range(1, m):
    for j in range(1, n):
        if string[1][i] == string[0][j]:
            arr[i][j] = arr[i-1][j-1]
        else:
            arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1

print(arr[m-1][n-1])


