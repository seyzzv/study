from itertools import permutations

def solution(expression):
    numbers = []
    operators = []
    curr = ""

    for char in expression:
        if char in "+-*":
            operators.append(char)
            numbers.append(int(curr))
            curr = ""
        else:
            curr += char
    numbers.append(int(curr))

    unique_operators = list(set(operators))
    max_val = 0

    for perm in permutations(unique_operators, len(unique_operators)):
        temp_nums = list(numbers)
        temp_ops = list(operators)

        for op in perm:
            while op in temp_ops:
                idx = temp_ops.index(op)
                if op == "+":
                    res = temp_nums[idx] + temp_nums[idx + 1]
                elif op == "-":
                    res = temp_nums[idx] - temp_nums[idx + 1]
                elif op == "*":
                    res = temp_nums[idx] * temp_nums[idx + 1]

                temp_nums[idx] = res
                temp_nums.pop(idx + 1)
                temp_ops.pop(idx)

        result = abs(temp_nums[0])
        if result > max_val:
            max_val = result

    return max_val