from collections import deque


def solution(priorities, location):
    priorities = deque(priorities)
    index = deque(list(range(0, len(priorities))))
    cnt = 0
    while True:
        m = max(priorities)
        while priorities[0] < m:
            priorities.append(priorities.popleft())
            index.append(index.popleft())
        while priorities[0] == m:
            priorities.popleft()
            i = index.popleft()
            cnt += 1
            if i == location:
                return cnt


print(solution([1, 1, 9, 1, 1, 1], 0))
