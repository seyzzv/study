def solution(phone_number):
    num = len(phone_number) - 4
    answer = '*' * num + phone_number[-4:]
    return answer