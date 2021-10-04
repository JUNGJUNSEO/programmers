def solution(clothes):
    d = dict()
    for cloth, kind in clothes:
        d[cloth] = kind
    answer = 0
    for i in d:
        for j in d:
            if d[i] == d[j]:
                continue
            answer += 1
    answer = len(d)+answer//2
    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses",
                                            "eyewear"], ["green_turban", "headgear"]]))
