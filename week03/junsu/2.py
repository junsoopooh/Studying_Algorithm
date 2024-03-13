def solution(participant, completion):
    arr = {}
    for runner in completion:
        if runner not in arr:
            arr[runner] = 1
        else:
            arr[runner] += 1
    for player in participant:
        if arr.get(player):
            arr[player] -= 1
        else:
            return player
