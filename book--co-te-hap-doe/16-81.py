"""
부분 배낭 문제
"""

# 각 물건의 단위 무게당 가치를 계산하여 items 리스트에 추가
def calculate_unit_value(items):
    for item in items:
        item.append(item[1] / item[0])

    return items


# 단위 무게당 가치가 높은 순으로 물건을 정렬
def sort_by_unit_value(items):
    items.sort(key = lambda x:x[2], reverse=True)

    return items


def knapsack(items, weight_limit):
    total_value = 0
    remaining_weight = weight_limit

    for item in items:
        if item[0] <= remaining_weight:
            total_value += item[1]
            remaining_weight -= item[0]
        else:
            fraction = remaining_weight / item[0]
            total_value += item[1] * fraction
            break

    return total_value



def solution(items, weight_limit):

    items = calculate_unit_value(items)
    items = sort_by_unit_value(items)

    return knapsack(items, weight_limit)

print(solution([[10, 19], [7, 10], [6, 10]], 15))       # 27.33
print(solution([[10, 60], [20, 100], [30, 120]], 50))   # 240