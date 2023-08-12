def solution(num_list):
    num1 = 0
    num2 = 0
    
    for i in num_list:
        if i%2 == 0:
            num1+=1
        else:
            num2+=1
    
    answer = [num1, num2]
    
    return answer