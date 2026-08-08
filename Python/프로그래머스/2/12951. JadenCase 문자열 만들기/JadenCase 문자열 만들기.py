def solution(s):
    answer = ""
    is_TF = True
    for ch in s:
        if ch == " ":
            answer += ch
            is_TF = True
        else:
            if is_TF:
                answer += ch.upper()
                is_TF = False
            else:
                answer += ch.lower()
    return answer