def solution(s):
    answer = ""
    lst = s.split(" ")
    for l in range(len(lst)):
        lst[l] = int(lst[l])

    maxStr = str(max(lst))
    minStr = str(min(lst))

    answer += minStr
    answer += " "
    answer += maxStr

    return answer
