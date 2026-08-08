def check(binary, start, end):
    if start >= end:
        return True
    
    mid = (start + end) // 2
    
    if binary[mid] == '0':
        if '1' in binary[start:mid] or '1' in binary[mid + 1:end + 1]:
            return False
            
    return check(binary, start, mid - 1) and check(binary, mid + 1, end)

def solution(numbers):
    answer = []
    
    for num in numbers:
        b = bin(num)[2:]
        
        length = len(b)
        size = 1
        while size < length:
            size = (size << 1) + 1
        
        b = b.zfill(size)
        
        answer.append(1 if check(b, 0, len(b) - 1) else 0)
        
    return answer