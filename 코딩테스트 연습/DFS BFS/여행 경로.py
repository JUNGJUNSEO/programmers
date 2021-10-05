def solution(tickets):
    d = dict()
    check = dict()
    for citys in tickets:
        check[str(citys)] = 0
    for citys in tickets:
        check[str(citys)] += 1
    for city_1, _ in tickets:
        d[city_1] = []
    for city_1, city_2 in tickets:
        d[city_1].append(city_2)
    for city_1, _ in tickets:
        d[city_1].sort()

    def dfs(city_1, cnt):
        if cnt == len(tickets):
            return 1
        if city_1 not in d:
            return
        for city_2 in d[city_1]:
            if check[str([city_1, city_2])] > 0:
                check[str([city_1, city_2])] -= 1
                answer.append(city_2)
                if dfs(city_2, cnt+1) == 1:
                    return 1
                answer.pop()
                check[str([city_1, city_2])] += 1
    answer = ["ICN"]
    dfs("ICN", 0)

    return answer


print(solution([["ICN", "COO"], ["ICN", "BOO"],
      ["COO", "ICN"], ["BOO", "DOO"]]))
