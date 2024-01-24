"""
리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘
예제 - 특정한 합읍 가지는 부분 연속 수열 찾기
"""

data = [1, 2, 3, 2, 5]
count = 0
n = 5       # 데이터의 개수
m = 5       # 찾고자 하는 부분합 M

interval_sum = 0
end = 0

# start 를 차례대로 증가시키며 반복
for start in range(n):
    # end 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    # 부분합이 m 일 때 카운트 증가
    if interval_sum == m:
        count += 1

    interval_sum -= data[start]

print(count)
