def solution(m, n, puddles):
    dx, dy = [1, 0], [0, 1]

    def dfs(x, y):
        if x == n-1 and y == m-1:
            return 1
        for i in range(2):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if dp[nx][ny] == 0:
                    dp[x][y] += dfs(nx, ny)
                elif dp[nx][ny] > 0:
                    dp[x][y] += dp[nx][ny]
        return dp[x][y]
    dp = [[0]*m for _ in range(n)]
    for x, y in puddles:
        dp[x-1][y-1] = -1
    answer = dfs(0, 0) % 1000000007

    return answer


print(solution(4, 4, [[3, 2], [2, 4]]), 7)
