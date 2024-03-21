from collections import deque

def solution(cacheSize, cities):
    que = deque()
    
    time = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower() # 대소문자 구분 안함
        if city in que:
            time += 1
            que.remove(city)
            que.appendleft(city)
        else:
            if len(que) < cacheSize:
                que.appendleft(city)
                time += 5
            else:
                que.pop()
                que.appendleft(city)
                time += 5
    
    return time
                