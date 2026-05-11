def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    
    left = 0
    right = distance
    
    while left <= right:
        mid = (left + right) // 2
        current = 0
        remove_count = 0
        
        for rock in rocks:
            diff = rock - current
            if diff < mid:
                remove_count += 1
            else:
                current = rock
                
        if remove_count <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return answer