# 캐시 https://school.programmers.co.kr/learn/courses/30/lessons/17680
# 1차 80/100
def solution(cacheSize, cities):
    answer = 0
    if not cacheSize:
        answer = 5 * len(cities)
        return answer
    arr = []
    for i in cities:
        city = i.lower()
        if len(arr) < cacheSize:
            answer += 5
            arr.append(city)
            continue

        if city in arr:
            answer += 1
            arr.remove(city)
            arr.append(city)
            continue
        else:
            answer += 5
            arr.pop(0)
            arr.append(city)
    return answer


# 2차 100/100


def solution(cacheSize, cities):
    answer = 0
    if not cacheSize:
        answer = 5 * len(cities)
        return answer
    arr = []
    for i in cities:
        city = i.lower()
        if len(arr) < cacheSize and city not in arr:
            answer += 5
            arr.append(city)
            continue

        if city in arr:
            answer += 1
            arr.remove(city)
            arr.append(city)
            continue
        else:
            answer += 5
            arr.pop(0)
            arr.append(city)
    return answer
