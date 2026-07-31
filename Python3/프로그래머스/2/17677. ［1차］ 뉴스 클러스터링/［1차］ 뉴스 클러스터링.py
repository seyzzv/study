import math
from collections import Counter

def solution(str1, str2):
    def make_multiset(s):
        s = s.lower()
        elements = []
        for i in range(len(s) - 1):
            pair = s[i:i+2]
            if pair.isalpha():
                elements.append(pair)
        return Counter(elements)

    set1 = make_multiset(str1)
    set2 = make_multiset(str2)
    
    if not set1 and not set2:
        return 65536

    intersection_size = sum((set1 & set2).values())
    union_size = sum((set1 | set2).values())

    jaccard = intersection_size / union_size
    return math.floor(jaccard * 65536)