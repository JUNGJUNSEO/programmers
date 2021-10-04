from itertools import permutations


def solution(numbers):
    MAX = 10000000
    check = [0]*(MAX+1)
    check[0] = check[1] = True
    for i in range(2, MAX+1):
        if check[i]:
            continue
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i
    n = len(numbers)
    a = []
    for i in range(n):
        a += map(int, map(''.join, (permutations(list(numbers), i+1))))
    answer = 0
    for x in set(a):
        if not check[x]:
            answer += 1
    return answer


print(solution("011"))
