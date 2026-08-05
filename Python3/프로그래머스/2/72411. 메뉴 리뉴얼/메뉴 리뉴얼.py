from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        comb_list = []
        for order in orders:
            sorted_order = sorted(order)
            comb_list.extend(combinations(sorted_order, c))

        comb_counts = Counter(comb_list)
        
        if comb_counts:
            max_count = max(comb_counts.values())
            if max_count >= 2:
                for comb, count in comb_counts.items():
                    if count == max_count:
                        answer.append(''.join(comb))
                        
    return sorted(answer)