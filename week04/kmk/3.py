"""
캐시
문제: https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""

"""
1. 캐시 사이즈 0이면 탐색하지말고 바로 반환 / 처음에 모든 도시 소문자로 변환
2. 캐시 히트인 경우 그냥 remove해주고 다시 맨뒤로 붙여줌(사이즈 최대 30이어서 remove해도 시간 복잡도에 영향 많이 X)
3. 캐시 미스인 경우 사이즈가 0보다 클때만 캐시에 넣어줌 만약 현재 캐시사이즈가 현재 큐에 사이즈와 같으면 맨 앞에서 하나 제거
"""
from collections import deque

def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5

    dq = deque()
    cities = [s.lower() for s in cities]
    run_time = 0

    for city in cities:
        if city not in dq:  # cache miss
            if len(dq) == cacheSize:
                dq.popleft()
            dq.append(city)
            run_time += 5
        else:  # cache hit
            dq.remove(city)
            dq.append(city)
            run_time += 1

    return run_time

"""
class Solution {
    public int solution(int cacheSize, String[] cities) {
        int runTime = 0;

        Queue<String> q = new LinkedList<>();

        for (int i = 0; i < cities.length; i++) {
            cities[i] = cities[i].toLowerCase();
        }

        List<String> cityList = new ArrayList<>(List.of(cities));

        for (String city : cityList) {

            if (!q.contains(city)) {
                if (cacheSize > 0) {
                    if (q.size() == cacheSize) {
                        q.poll();
                    }
                    q.add(city);
                }
                runTime += 5;
            } else {
                q.remove(city);
                q.add(city);
                runTime++;
            }

        }

        return runTime;
    }
}
"""

