from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    total_sum = sum1 + sum2
    
    # 전체 합이 홀수면 절반으로 나눌 수 없음
    if total_sum % 2 != 0:
        return -1
    
    target = total_sum // 2
    
    # 최대 시도 횟수 설정 ( queue1 길이 * 4 )
    max_operations = len(queue1) * 4
    operations = 0
    
    while operations <= max_operations:
        if sum1 == target:
            return operations
        
        if sum1 > target:
            val = q1.popleft()
            q2.append(val)
            sum1 -= val
            sum2 += val
        else:
            val = q2.popleft()
            q1.append(val)
            sum2 -= val
            sum1 += val
            
        operations += 1
        
    return -1