def solution(myStr):
    answer = []
    temp = ""
    for ch in myStr:
        if ch in ['a','b','c']:
            if temp != "":
                answer.append(temp)
            temp = ""
        else:
            temp += ch
    if temp != "":
        answer.append(temp)
    if not answer:
        return ["EMPTY"]
    return answer