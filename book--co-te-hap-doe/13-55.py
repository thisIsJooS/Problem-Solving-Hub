"""
이미 정렬이 완료되어 있는 두 배열 arr1, arr2 를 받아 병합 정렬하는 solution() 함수를 구현하라
"""
"""
arr1  /  arr2   / return
135   /  246    / 123456
123   /  456    / 123456
"""

def solution(arr1, arr2):
    arr = []

    while arr1 or arr2:
        if arr1 and arr2:
            if arr1[0] < arr2[0]:
                arr.append(arr1.pop(0))
            else:
                arr.append(arr2.pop(0))
        elif arr1:
            arr.append(arr1.pop(0))
        else:
            arr.append(arr2.pop(0))

    return arr



print(solution([1, 3, 5], [2, 4, 6]))
print(solution([1, 2, 3], [4, 5, 6]))