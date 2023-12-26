def binary_search(arr, target, start, end):
    if start > end:     # 재귀함수니까 중단점을 제공해줘야 함
        return None

    mid = (start + end) // 2

    if arr[mid] == target:      # 찾은 경우 중간점 인덱스 반환
        return mid

    elif arr[mid] > target:     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        return binary_search(arr, target, start, mid-1)

    else:                       # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        return binary_search(arr, target, mid+1, end)


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target = 9
result = binary_search(arr, target, 0, len(arr)-1)

print(result+1) if result else print('원소가 존재하지 않음')