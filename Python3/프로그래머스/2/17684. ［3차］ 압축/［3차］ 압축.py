def solution(msg):
    answer = []
    
    dictionary = {chr(i): i - 64 for i in range(65, 91)}
    next_index = 27
    
    i = 0
    while i < len(msg):
        w = ""
        while i < len(msg) and w + msg[i] in dictionary:
            w += msg[i]
            i += 1
            
        answer.append(dictionary[w])
        
        if i < len(msg):
            c = msg[i]
            dictionary[w + c] = next_index
            next_index += 1
            
    return answer