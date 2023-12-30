# 9분 15초 - 12월 29일
"""
x , +를 넣어 만들수 있는 가장 큰 수를 구하라.
사칙연산 없고

02984
"""
data = input()
arr = []
for d in data:
    arr.append(int(d))
n = len(arr)

res = arr[0]

for i in range(1, n):
    if arr[i] == 0 or arr[i] == 1 or res == 0 or res == 1:
        res += arr[i]
    else:
        res *= arr[i]

print(res)