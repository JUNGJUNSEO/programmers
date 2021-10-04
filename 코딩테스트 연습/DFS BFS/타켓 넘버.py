def solution(numbers, target):
    def go(n, sum):
        if n == len(numbers):
            if sum == target:
                return 1
            return 0
        return go(n+1, sum+numbers[n])+go(n+1, sum-numbers[n])
    answer = go(0, 0)
    return answer
