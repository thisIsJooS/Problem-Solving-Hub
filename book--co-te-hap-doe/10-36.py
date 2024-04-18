def _solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: -len(x))

    dic = {}

    for pn in phone_book:
        if pn in dic:
            return False

        for i in range(1, len(pn) + 1):
            chunk = pn[:i]

            dic[chunk] = True

    return answer

"""
테스트 1 〉	통과 (25.06ms, 17.8MB)
테스트 2 〉	통과 (23.34ms, 17.9MB)
테스트 3 〉	통과 (568.63ms, 48.2MB)
테스트 4 〉	통과 (887.88ms, 236MB)
"""


def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True

"""
테스트 1 〉	통과 (2.91ms, 10.6MB)
테스트 2 〉	통과 (2.92ms, 10.7MB)
테스트 3 〉	통과 (153.68ms, 30.6MB)
테스트 4 〉	통과 (85.54ms, 28.1MB)
"""