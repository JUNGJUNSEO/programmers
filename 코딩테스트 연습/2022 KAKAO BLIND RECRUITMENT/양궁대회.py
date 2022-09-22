from itertools import *


def solution(n, info):
    ret = [-1]*12
    for comb in combinations_with_replacement(range(11), n):
        temp = [0]*12
        for i in comb:
            temp[i] += 1
        score = 0
        for i in range(11):
            if temp[i] > info[i]:
                score += (10-i)
            elif info[i] != 0:
                score -= (10-i)
        if score <= 0:
            continue

        temp[11] = score

        if temp[::-1] > ret[::-1]:
            ret = temp[:]

    return ret[:-1] if sum(ret[:]) != -12 else [-1]
