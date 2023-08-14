# 런타임 에러
# def solution(N, stages):
#     hash = {}
#     trash = []
#     for i in range(1,N+1):
#         if i in stages:
#             trash.append(i)
#             hash[i]= stages.count(i)/len(stages)
#             stages = [i for i in stages if i not in trash]
#         else:
#             hash[i] = 0/len(stages)
#     return list(dict(sorted(hash.items(), key=lambda x: x[1], reverse = True)).keys

def solution(N, stages):
    hash = {}
    for i in range(1,N+1):
        if i in stages:
            hash[i]= stages.count(i)/len(stages)
            stages = list(filter((i).__ne__, stages))
        else:
            if len(stages)==0:
              hash[i] = 0
            else:
              hash[i] = 0/len(stages)

    return list(dict(sorted(hash.items(), key=lambda x: x[1], reverse = True)).keys())