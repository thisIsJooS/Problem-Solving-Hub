arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return

    pivot = start       # 일단 피벗은 첫번째 원소 (by Hoare Partition)
    left, right = start+1, end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:  # 피벗보다 큰 데이터를 찾을 때 까지 반복
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:            # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:                       # 엇갈리지 않았다면 작은 데이터와 피벗을 교체
            arr[left], arr[right] = arr[right], arr[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


quick_sort(arr, 0, len(arr)-1)
print(arr)