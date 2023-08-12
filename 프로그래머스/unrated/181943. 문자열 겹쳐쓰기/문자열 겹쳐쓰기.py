# 기존에 내가 푼 방법
# def solution(my_string, overwrite_string, s):
#     n = len(overwrite_string) + s
#     answer = my_string.replace(my_string[s:n], overwrite_string)
#     return answer

def solution(my_string, overwrite_string, s):
    n = len(overwrite_string) + s
    t1,t2,t3 = my_string[:s],my_string[s:n],my_string[n:] 
    answer = t1+overwrite_string+t3
    return answer