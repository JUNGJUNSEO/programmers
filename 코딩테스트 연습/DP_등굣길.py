from collections import deque


def solution(m, n, puddles):
    dx, dy = [1, 0], [0, 1]

    def go(x, y):
        if check[x][y] == 1:
            return 1
        check[x][y] = 1
        if x == n-1 and y == m-1:
            return 1
        ans = 0
        for i in range(2):
            nx, ny = x+dx[i], y+dy[i]
            if nx == n or ny == m:
                continue
            if check[nx][ny] == 0 or check[nx][ny] == 1:
                ans += go(nx, ny)
        return ans
    check = [[0]*m for _ in range(n)]
    for y, x in puddles:
        check[x-1][y-1] = -1
    answer = go(0, 0)
    return answer


print(solution(100, 100, []), 690285631)
