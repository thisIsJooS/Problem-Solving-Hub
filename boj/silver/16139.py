# import sys
# input = sys.stdin.readline
#
# s = input()
# n = int(input())
#
# arr = [0] * len(s)
#
#
# for i in range(n):
#     c, left, right = input().split()
#
#     count = 0
#     for k in range(len(s)):
#         if s[k] == c:
#             count += 1
#         arr[k] = count
#
#     arr.append(0)
#     made = True
#
#     left, right = map(int, (left, right))
#     print(arr[right] - arr[left-1])
#
# =--------------------50점


import sys
input = sys.stdin.readline
from bisect import *

string = list(input().rstrip())
n = int(input())

location = [[] for _ in range(26)]

for i in range(len(string)):
    c = string[i]
    index = ord(c) - ord('a')
    location[index].append(i)


for i in range(n):
    c, left, right = input().split()
    left, right = map(int, (left, right))

    locations = location[ord(c) - ord('a')]
    l = bisect_left(locations, left)
    r = bisect_right(locations, right)

    print(r-l)




