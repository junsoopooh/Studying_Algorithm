def solution(n):
    answer = []
    st = str(n)
    answer = list(st)
    result = []
    for i in range(-1,-len(answer)-1,-1):
        print(answer[i])
        result.append(int(answer[i]))
    return result

