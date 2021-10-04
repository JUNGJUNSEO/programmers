from collections import deque


def solution(pro, speeds):
    pro, speeds = deque(pro), deque(speeds)
    answer = []
    while pro:
        for i in range(len(pro)):
            pro[i] += speeds[i]
        cnt = 0
        while pro and pro[0] >= 100:
            pro.popleft()
            speeds.popleft()
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    return answer


print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]))
