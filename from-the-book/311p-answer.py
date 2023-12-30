"""
x인 사람은 x명 이상의 그룹에 참여해야함
그룹수의 최대값
"""
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = 0
cnt = 0

for i in arr:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0

print(res)

"""
40
3 2 2 1 3 3 2 1 1 4 1 2 3 2 2 3 1 1 3 2 2 3 3 2 1 4 1 2 3 2 2 3 1 1 3 2 2 3 2 2
"""