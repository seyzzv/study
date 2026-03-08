def solution(progresses, speeds):
    days = []
    
    for p, s in zip(progresses, speeds):
        days.append((100 - p + s - 1) // s)
    
    answer = []
    current = days[0]
    count = 1
    
    for i in range(1, len(days)):
        if days[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = days[i]
            count = 1
    
    answer.append(count)
    
    return answer