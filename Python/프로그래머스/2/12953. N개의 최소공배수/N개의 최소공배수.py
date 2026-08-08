def solution(arr):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b // gcd(a, b)
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)
    return result