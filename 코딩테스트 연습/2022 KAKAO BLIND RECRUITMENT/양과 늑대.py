val = []
ans = 0
a = [[] for _ in range(17)]
check = [False]*(1 << 17)


def dfs(s_lst, w_lst):
    global ans

    if len(w_lst) >= len(s_lst):
        return

    ans = max(ans, len(s_lst))

    t = 0
    t_lst = s_lst+w_lst
    for i in t_lst:
        t += (1 << i)
    check[t] = True

    for p in t_lst:
        for c in a[p]:

            if (t & (1 << c)) or check[t + (1 << c)]:
                continue
            # 양
            if val[c] == 0:
                dfs(s_lst+[c], w_lst)
            # 늑대
            else:
                dfs(s_lst, w_lst+[c])


def solution(info, edges):
    global val
    val = info

    for u, v in edges:
        a[u].append(v)

    dfs([0], [])
    return ans
