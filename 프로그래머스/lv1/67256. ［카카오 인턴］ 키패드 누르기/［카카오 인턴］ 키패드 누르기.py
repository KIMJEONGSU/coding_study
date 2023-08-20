import math
def solution(numbers, hand):
    answer = ''
    phone = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}

    left_current = phone['*']
    right_current = phone['#']

    for i in numbers:
      if i in [1,4,7]:
        answer += 'L'
        left_current = phone[i]
      elif i in [3,6,9]:
        answer += 'R'
        right_current = phone[i]
      elif i in [2,5,8,0]:
        if abs(left_current[0]-phone[i][0]) + abs(phone[i][1]-left_current[1]) == abs(right_current[0]-phone[i][0]) + abs(phone[i][1]-right_current[1]):
          if hand == 'left':
            answer += 'L'
            left_current = phone[i]
          elif hand == 'right':
            answer += 'R'
            right_current=phone[i]
        elif abs(left_current[0]-phone[i][0]) + abs(phone[i][1]-left_current[1]) > abs(right_current[0]-phone[i][0]) + abs(phone[i][1]-right_current[1]):
          answer+='R'
          right_current = phone[i]
        else:
          answer+='L'
          left_current = phone[i]
    return answer