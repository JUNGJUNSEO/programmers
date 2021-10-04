from collections import deque


def solution(n, edge):
    a = [[] for _ in range(n)]
    for x, y in edge:
        a[x-1].append(y-1)
        a[y-1].append(x-1)
    dist = [0]*(n)
    dist[0] = 1
    q = deque()
    q.append(0)
    while q:
        x = q.popleft()
        for i in a[x]:
            if dist[i] != 0:
                continue
            dist[i] = dist[x]+1
            q.append(i)
    answer = dist.count(max(dist))
    return answer
