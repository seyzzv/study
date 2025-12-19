def solution(order):
    answer = 0
    for i in order:
        if i == "anything":
            answer += 4500
        elif "americano" in i:
            answer += 4500
        elif "cafelatte" in i:
            answer += 5000
    return answer