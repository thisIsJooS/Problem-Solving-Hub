#https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    # 1.해시 테이블 생성
    dic = {}

    # 2.참가자들의 이름을 해시 테이블에 추가
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1

    # 3.완주한 선수들의 이름을 키로 하는 값을 1씩 감소
    for c in completion:
        dic[c] -= 1

    # 4.해시 테이블에 남아 있는 선수가 완주하지 못한 선수
    for key in dic.keys():
        if dic[key] > 0:
            return key



