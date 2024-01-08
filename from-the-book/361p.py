def solution(N, stages):
    length = len(stages)
    answer = []
    rates = []
    prev_cleared = length
    for i in range(1, N + 1):
        if prev_cleared == 0:
            rates.append((0, i))
            continue

        rate = stages.count(i) / prev_cleared
        prev_cleared -= stages.count(i)

        rates.append((rate, i))

    rates.sort(key=lambda x: x[0], reverse=True)

    for r in rates:
        answer.append(r[1])

    return answer