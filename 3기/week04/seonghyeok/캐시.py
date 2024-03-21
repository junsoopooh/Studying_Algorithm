from collections import deque


def solution(cacheSize, cities):
    # 소문자 변경
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    answer = 0
    cacheQ = deque()
    if cacheSize == 0:
        return len(cities) * 5
    else:
        cacheQ.append(cities[0])
        answer += 5

    for i in range(1, len(cities)):
        # size over
        if len(cacheQ) >= cacheSize:
            # cache Hit
            if cities[i] in cacheQ:
                cacheQ.remove(cities[i])
                cacheQ.appendleft(cities[i])
                answer += 1
            # cache Miss
            else:
                answer += 5
                cacheQ.pop()
                cacheQ.appendleft(cities[i])
        else:
            # cache Hit
            if cities[i] in cacheQ:
                cacheQ.remove(cities[i])
                cacheQ.appendleft(cities[i])
                answer += 1
            # cache Miss
            else:
                answer += 5
                cacheQ.appendleft(cities[i])

    return answer