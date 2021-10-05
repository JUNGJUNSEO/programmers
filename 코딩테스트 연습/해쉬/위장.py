def solution(clothes):
    d = dict()
    for _, kind in clothes:
        if kind in d:
            d[kind] += 1
        else:
            d[kind] = 1
    a = list(d.values())
    answer = 1
    for cnt in a:
        answer = answer*(cnt+1)
    return answer-1
