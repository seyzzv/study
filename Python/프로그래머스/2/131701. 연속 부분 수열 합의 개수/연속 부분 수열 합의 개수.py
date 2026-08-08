def solution(elements):
    n = len(elements)
    extended = elements * 2
    result = set()
    
    # 부분 수열 길이 1 ~ n
    for length in range(1, n + 1):
        # 시작 인덱스
        for start in range(n):
            sub_sum = sum(extended[start:start + length])
            result.add(sub_sum)
    return len(result)