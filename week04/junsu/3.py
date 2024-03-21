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
    # 캐시가 없을 떄는 모든 동작이 5초 걸리는 것으로 계산하여 결과 도출
    if not cacheSize:
        answer = 5 * len(cities)
        return answer
    # 캐시 배열
    arr = []
    for i in cities:
        # 소문자로 통일
        city = i.lower()
        # 아직 캐시에 여유 자리가 있고, 캐시에 존재하지 않는 도시인 경우만 캐시에 추가한다.
        if len(arr) < cacheSize and city not in arr:
            answer += 5
            arr.append(city)
            continue

        # 캐시에 여유자리가 없거나, 여유 자리가 있지만 이미 캐시에 존재하는 도시의 경우 로직의 흐름
        # 캐시에 있는 도시의 경우 캐시에서 가장 마지막 index로 설정해준다.
        if city in arr:
            answer += 1
            arr.remove(city)
            arr.append(city)
            continue
        # 캐시에 없을 경우 0번 index를 삭제하고 새로운 캐시를 마지막 index에 추가해준다.
        else:
            answer += 5
            arr.pop(0)
            arr.append(city)
    return answer
