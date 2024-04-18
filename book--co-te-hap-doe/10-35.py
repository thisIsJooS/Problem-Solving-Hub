# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    pnum, round = 0, 0
    prev = ''
    hist = set()

    for i, word in enumerate(words):

        if prev and (word in hist or prev[-1] != word[0]):
            pnum = i % n + 1
            round = i // n + 1
            break

        prev = word
        hist.add(prev)

    return [pnum, round]