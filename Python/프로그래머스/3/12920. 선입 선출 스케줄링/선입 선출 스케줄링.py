def solution(n, cores):
    if n <= len(cores):
        return n
    
    left = 0
    right = min(cores) * n
    time = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        count = len(cores)
        for core in cores:
            count += mid // core
            
        if count >= n:
            time = mid
            right = mid - 1
        else:
            left = mid + 1

    work_count = len(cores)
    for core in cores:
        work_count += (time - 1) // core
        
    for i in range(len(cores)):
        if time % cores[i] == 0:
            work_count += 1
            
            if work_count == n:
                return i + 1