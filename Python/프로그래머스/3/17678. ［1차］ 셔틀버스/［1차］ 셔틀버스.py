def solution(n, t, m, timetable):
    minutes = []
    for time in timetable:
        h, mi = map(int, time.split(':'))
        minutes.append(h * 60 + mi)
    minutes.sort()
    
    bus_time = 9 * 60
    crew_idx = 0
    
    for i in range(n):
        ride_cnt = 0
        while ride_cnt < m and crew_idx < len(minutes) and minutes[crew_idx] <= bus_time:
            ride_cnt += 1
            crew_idx += 1
            
        if i == n - 1:
            if ride_cnt < m:
                ans_time = bus_time
            else:
                ans_time = minutes[crew_idx - 1] - 1
        
        bus_time += t
        
    h = str(ans_time // 60).zfill(2)
    mi = str(ans_time % 60).zfill(2)
    return f"{h}:{mi}"