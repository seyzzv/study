def solution(arr):
    answer = 0
    while True:
        changed = False
        for i in range(len(arr)):
            x = arr[i]
            if x >= 50 and x % 2 == 0:
                arr[i] = x // 2
                changed = True
            elif x < 50 and x % 2 == 1:
                arr[i] = x * 2 + 1
                changed = True
        if not changed:
            return answer
        answer += 1