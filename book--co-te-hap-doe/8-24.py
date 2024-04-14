# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []

    reported_count = {}
    report_history = {}
    for r in report:
        reporter, reportee = r.split()
        if reportee not in reported_count:
            reported_count[reportee] = 1
        else:
            if reporter in report_history and reportee in report_history[reporter]:
                pass
            else:
                reported_count[reportee] += 1

        if reporter not in report_history:
            report_history[reporter] = {reportee}
        else:
            report_history[reporter].add(reportee)

    reported_result = {}
    for reportee in reported_count:
        if reported_count[reportee] >= k:
            reported_result[reportee] = True

    for i, userId in enumerate(id_list):
        if userId not in report_history:
            answer.append(0)
            continue

        cnt = 0
        for reportee in report_history[userId]:
            if reportee in reported_result:
                cnt += 1

        answer.append(cnt)

    return answer