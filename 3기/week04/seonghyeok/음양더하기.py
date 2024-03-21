def solution(absolutes, signs):
    result = []
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            result.append(absolutes[i])
        else:
            result.append(-absolutes[i])
    answer = sum(result)
    return answer