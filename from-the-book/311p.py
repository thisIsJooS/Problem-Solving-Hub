"""
x인 사람은 x명 이상의 그룹에 참여해야함
그룹수의 최대값
"""
n = int(input())
arr = list(map(int, input().split()))

"""
2 3 1 2 2  -> 2

3 2 2 2 1
"""
arr.sort(reverse=True)

res = 0
i = 0
while i < n:
    res += 1
    i += arr[i]

print(res)

"""
5
2 3 1 2 2
"""