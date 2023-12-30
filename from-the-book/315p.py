"""
무게 : 1~M
서로 수가 달라야 함
"""
n, m = map(int, input().split())

arr = list(map(int, input().split()))
count = [0] * 11

for a in arr:
    count[a] += 1

res = 0
for i in range(1, m+1): # 볼링공 무게
    if count[i] != 0:
        res += count[i] * (n-count[i])

print(res//2)
