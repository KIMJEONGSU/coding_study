def solution(numbers):
    max_num = sorted(numbers)[-2:]
    answer = max_num[0] * max_num[1]
    return answer