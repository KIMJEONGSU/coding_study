def solution(n):
    first = 2
    answer = [i for i in range(first, n+1, 2)]
    return sum(answer)