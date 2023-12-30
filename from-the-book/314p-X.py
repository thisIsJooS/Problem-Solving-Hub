"""
합쳐서 만들수 없어야 함
"""
n = int(input())
data = list(map(int, input().split()))

"""
3 2 1 1 9 -> 8
1 1 2 3 9
"""
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

