def solution(sequence, k):
    n = len(sequence)
    left = 0
    right = 0
    current_sum = sequence[0]

    best_range = [0, n - 1, n]
    
    while left < n and right < n:
        if current_sum == k:
            length = right - left
            if length < best_range[2]:
                best_range = [left, right, length]
            current_sum -= sequence[left]
            left += 1
        elif current_sum < k:
            right += 1
            if right < n:
                current_sum += sequence[right]
        else:
            current_sum -= sequence[left]
            left += 1
            
    return [best_range[0], best_range[1]]