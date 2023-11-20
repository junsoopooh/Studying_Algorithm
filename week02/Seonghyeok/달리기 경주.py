def solution(players, callings):
    resultLst = dict()

    for i in range(len(players)):
        resultLst[players[i]] = i


    for i in callings:
        idx = resultLst[i]

        # 스왑과정 && callings의 target전 값을 key에저장(dic의 idx조정을위해)
        tmp = players[idx]
        key = players[idx-1]

        players[idx] = players[idx-1]
        players[idx-1] = tmp

        # dic 인덱스 조정
        resultLst[tmp] = idx-1
        resultLst[key] = idx

    return players
