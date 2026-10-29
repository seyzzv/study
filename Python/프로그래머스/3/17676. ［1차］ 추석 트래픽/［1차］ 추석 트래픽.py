def solution(lines):
    logs = []

    for line in lines:
        date, time, duration = line.split()
        h, m, s = time.split(':')
        end = (int(h) * 3600 + int(m) * 60) * 1000 + int(float(s) * 1000)
        process = int(float(duration[:-1]) * 1000)
        logs.append((end - process + 1, end))

    answer = 0

    for _, end in logs:
        start = end
        finish = start + 999
        count = sum(1 for s, e in logs if s <= finish and e >= start)
        answer = max(answer, count)

    return answer