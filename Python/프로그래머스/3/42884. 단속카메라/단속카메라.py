def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera_pos = -30001
    answer = 0
    
    for route in routes:
        if camera_pos < route[0]:
            answer += 1
            camera_pos = route[1]
            
    return answer