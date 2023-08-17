import re
def solution(dartResult):
    answer = []
    p = re.compile('(\d+)(\D)(\D?)')
    dar_list = p.findall(dartResult)
    print(dar_list)
    star = 0

    for i in range(len(dar_list)):

        if star>0 and dar_list[i][2]=='*':
          answer[i-1]*=2

        if dar_list[i][1] == 'S':
          answer.append(int(dar_list[i][0])**1)
          star+=1
          if dar_list[i][2]=='#':
            answer[i]*=(-1)
          elif dar_list[i][2]=='*':
            answer[i]*=2
          print(answer)
        elif dar_list[i][1] == 'D':
          answer.append(int(dar_list[i][0])**2)
          star+=1
          if dar_list[i][2]=='#':
            answer[i]*=(-1)
          elif dar_list[i][2]=='*':
            answer[i]*=2
          print(answer)
        elif dar_list[i][1] == 'T':
          answer.append(int(dar_list[i][0])**3)
          star+=1
          if dar_list[i][2]=='#':
            answer[i]*=(-1)
          elif dar_list[i][2]=='*':
            answer[i]*=2
          print(answer)

    return sum(answer)
# 다른사람의 코드를 보고 이해하려고함.
# import re
# def solution(dartResult):
#     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
#     option = {'' : 1, '*' : 2, '#' : -1}
#     p = re.compile('(\d+)([\D])([\D]?)')
#     dart = p.findall(dartResult)
#     for i in range(len(dart)):
#       if dart[i][2]=='*' and i>0:
#         dart[i-1]*=2
#       dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
#     return sum(dart)
