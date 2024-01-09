from bisect import *

arr = [0, 1, 2, 3, 4, 5, 6, 8, 9]
print(bisect_left(arr, 7))
print(bisect_right(arr, 7))