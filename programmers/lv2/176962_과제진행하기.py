# https://school.programmers.co.kr/learn/courses/30/lessons/176962#

from collections import deque

def solution(plans):
    answer = []

    for i in range(len(plans)):
        plan = plans[i]
        plan[2] = int(plan[2])
        plan[1] = to_minute(plan[1])
        plans[i] = plan

    plans.sort(key=lambda x: x[1])

    tasks = deque(plans)
    waiting = deque()

    while tasks:
        task = tasks.popleft()
        name, start, playtime = task

        end_time = start + playtime

        if tasks:  # 마지막 일이 아니라면
            next_name, next_start, next_playtime = tasks[0]

            if end_time > next_start:  # 아직 끝나지 않았는데, 다음 일이 시작해야 한다.
                waiting.append((name, start, playtime - (next_start - start)))
                continue

            # 다음 일이 시작되기 전에 일을 마쳤다.
            answer.append(name)

            # 다음 일까지 남은 시간
            remained_time = next_start - end_time

            # 대기중인 작업이 있다면 꺼내서 일을 한다. 
            while waiting:
                waiting_task = waiting.pop()
                waiting_name, waiting_start, waiting_playtime = waiting_task

                if remained_time < waiting_playtime:  # 대기중인 작업을 여전히 끝낼 수 없을 때
                    waiting.append((waiting_name, waiting_start, waiting_playtime - remained_time))
                    break

                else:  # 대기중인 작업을 끝낼 수 있을 때
                    answer.append(waiting_name)  # 끝내고, 또 다음 대기중인 작업을 시작해야 한다.
                    remained_time -= waiting_playtime

        else:  # 마지막 일이었다면
            answer.append(name)

    while waiting:  # 남은것들을 순서대로 끝낸다.
        waiting_task = waiting.pop()
        answer.append(waiting_task[0])

    return answer


def to_minute(time):
    arr = list(map(int, time.split(":")))

    return arr[0] * 60 + arr[1]




