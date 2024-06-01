# https://school.programmers.co.kr/learn/courses/30/lessons/155651#

def solution(book_time):
    arr = []

    book_time.sort()

    for book in book_time:
        if not arr:
            arr.append(book)
            continue

        for i, a in enumerate(arr):
            if not g(a, book):
                arr[i] = book
                break
        else:
            arr.append(book)

    return len(arr)


def g(gijon, new):
    gijon_end = plus_10m(gijon[1])
    new_end = new[0]

    if int(new_end[:2]) < int(gijon_end[:2]):
        return True
    elif int(new_end[:2]) == int(gijon_end[:2]):
        if int(new_end[3:]) < int(gijon_end[3:]):
            return True

    return False


def plus_10m(time):
    hour = int(time[:2])
    minute = int(time[3:])

    minute += 10

    if minute >= 60:
        hour += 1
        minute -= 60

    if hour < 10:
        hour = f'0{hour}'

    return f'{hour}:{minute}'
