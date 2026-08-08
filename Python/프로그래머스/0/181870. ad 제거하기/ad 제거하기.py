def solution(strArr):
    result = []
    for s in strArr:
        if "ad" not in s:
            result.append(s)
    return result