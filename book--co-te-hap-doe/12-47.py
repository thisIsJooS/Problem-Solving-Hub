"""
정수 N을 입력받아 1부터 N 까지의 숫자 중에서 합이 10이 되는 조합을 리스트로 반환
"""

def solution(N):
    results = []

    def bt(sum, selected_nums, start):
        if sum == 10:
            results.append(selected_nums)
            return

        for i in range(start, N+1):
            if sum + i <= 10:
                bt(sum+i, selected_nums + [i], i+1)

    bt(0, [], 1)

    return results


print(solution(5))
print(solution(2))
print(solution(7))

"""
    [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]]
    []
    [[1, 2, 3, 4], [1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5], [3, 7], [4, 6]]
"""