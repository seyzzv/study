def solution(a, b, c, d):
    dice = [a, b, c, d]
    count = {}
    for num in dice:
        count[num] = count.get(num, 0) + 1
    kinds = len(count)
    if kinds == 1:
        p = dice[0]
        return 1111 * p
    elif 3 in count.values():
        for num in count:
            if count[num] == 3:
                p = num
            else:
                q = num
        return (10 * p + q) ** 2
    elif kinds == 2:
        nums = list(count.keys())
        if count[nums[0]] == 2 and count[nums[1]] == 2:
            p, q = nums[0], nums[1]
            return (p + q) * abs(p - q)
    elif 2 in count.values():
        p = 0
        others = []
        for num in count:
            if count[num] == 2:
                p = num
            else:
                others.append(num)
        q, r = others
        return q * r
    else:
        return min(dice)