# 달리기 경주

def solution(players, callings):
    arr = {}
    for i in range(len(players)):
        arr[players[i]] = i
    for call in callings:
        rank = arr[call]
        arr[call] -= 1
        arr[players[rank-1]] += 1
        a = players[rank]
        b = players[rank-1]
        players[rank] = b
        players[rank-1] = a
    return players
