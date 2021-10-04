def solution(lottos, win_nums):
    count_zero = lottos.count(0)
    count_win_nums = 0
    for i in range(6):
        if lottos[i] in win_nums:
            count_win_nums += 1
    a = 7-(count_zero+count_win_nums)
    b = 7-count_win_nums
    if a > 5:
        a = 6
    if b > 5:
        b = 6
    answer = [a,b]
    return answer
lottos = map(int,sys.stdin.readline().split())
win_nums = map(int,sys.stdin.readline().split())
print(solution(lottos, win_nums))
