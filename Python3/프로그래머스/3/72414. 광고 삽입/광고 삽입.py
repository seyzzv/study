def to_sec(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def to_str(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def solution(play_time, adv_time, logs):
    play_sec = to_sec(play_time)
    adv_sec = to_sec(adv_time)
    
    if play_sec == adv_sec:
        return "00:00:00"

    total = [0] * (play_sec + 1)

    for log in logs:
        start, end = log.split('-')
        s_sec, e_sec = to_sec(start), to_sec(end)
        total[s_sec] += 1
        total[e_sec] -= 1

    for i in range(1, play_sec + 1):
        total[i] += total[i - 1]

    for i in range(1, play_sec + 1):
        total[i] += total[i - 1]

    max_val = total[adv_sec - 1]
    best_time = 0

    for start in range(1, play_sec - adv_sec + 1):
        curr_val = total[start + adv_sec - 1] - total[start - 1]
        if curr_val > max_val:
            max_val = curr_val
            best_time = start

    return to_str(best_time)