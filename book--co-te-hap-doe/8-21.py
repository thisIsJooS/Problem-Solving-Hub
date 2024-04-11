# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    nicks = {}

    for r in record:
        if r.startswith("Enter") or r.startswith("Change"):
            arr = r.split()
            uid, nickname = arr[1], arr[2]
            nicks[uid] = nickname

    for r in record:
        arr = r.split(' ')
        uid = arr[1]

        if r.startswith("Enter"):
            answer.append(f"{nicks[uid]}님이 들어왔습니다.")

        elif r.startswith("Leave"):
            answer.append(f"{nicks[uid]}님이 나갔습니다.")

    return answer