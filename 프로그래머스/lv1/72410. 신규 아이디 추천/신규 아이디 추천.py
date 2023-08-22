import re
def solution(new_id):
    tmp_1 = new_id.lower()
    tmp_2 = re.sub("[^-_.a-z0-9]", '', tmp_1)
    tmp_3 = re.sub(r"[.]{2,}", '.', tmp_2)
    tmp_4 = re.sub(r"^[.]|[.]$", '', tmp_3)
    if len(tmp_4)==0:
      tmp_4+='a'
    if len(tmp_4)>=16:
      tmp_4 = tmp_4[:15]
      tmp_4 = re.sub(r"^[.]|[.]$", '', tmp_4)
    if len(tmp_4)<3:
      while len(tmp_4)<3:
        tmp_4+=tmp_4[-1]
    
    return tmp_4