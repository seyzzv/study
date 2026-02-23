def solution(clothes):
    dic = {}
    
    for item in clothes:
        kind = item[1]
        
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1
    answer = 1
    
    for kind in dic:
        answer *= (dic[kind] + 1)
    
    return answer - 1