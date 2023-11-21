# 초기코드
def solution(players, callings):
    result = []
    # callings 배열을 돌면서 해당 선수의 하나씩 players 배열의 인덱스를 검사
    # 해당 인덱스에 인덱스-1의 값을 넣고
    # 인덱스-1에는 해당 선수를 넣어줌
    for i in callings:
        idx = players.index(i)
        if idx != 0:
            players[idx] = players[idx-1]
            players[idx-1] = i
            # print(players)
    return players

# 풀이코드
def solution(players, callings):
    result = {player: i for i, player in enumerate(players)}
    for who in callings:
        idx = result[who]
        result[who] -= 1
        result[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players