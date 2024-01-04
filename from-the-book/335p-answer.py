from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = 1e9

    # 0부터 length-1 까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):     # 친구들을 나열하는 경우의 수
            count = 1       # 투입할 친구의 수
            position = weak[start] + friends[count - 1]     # 그 친구가 점검할 수 있는 마지막 위치

            for index in range(start, start+length):    # 시작점부터 모든 취약지점을 확인
                if position < weak[index]:  # 점검할 수 있는 위치를 벗어나는 경우
                    count += 1      # 새 친구 투입
                    if count > len(dist):       # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]

            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer