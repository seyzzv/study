def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                total = nums[i] + nums[j] + nums[k]

                is_prime = True
                for n in range(2, int(total ** 0.5) + 1):
                    if total % n == 0:
                        is_prime = False
                        break

                if is_prime:
                    answer += 1

    return answer