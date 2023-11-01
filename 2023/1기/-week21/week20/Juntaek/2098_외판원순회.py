# n번까지의 번호가 매겨져 있는 도시
# 도시 사이에는 길 있거나 ㅓㅄ거나
# n개의 도시를 모두 거쳐 다시 원래 도시로 돌아오는 순회 여행 경로
# 단, 한번 갔던 도시로는 다시 못가.
# 출발했던 도시로 돌아오는 것은 예외
# 가장 적은 비용 들이는 여행 계획
# W[i][j]는 도시 i에서 도시 j로 가기 위한 비용
# 가장 적은 비용을 들이는 외판원 순회 여행 경로를 구하는 프로그램!

# 풀이 코드
import sys

input = sys.stdin.readline
n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]
VISITED_ALL = (1 << n) - 1

dp = [[None] * (1 << n) for _ in range(n)]
INF = float('inf')
idx = 1

def find_path(last, visited):
  if visited == VISITED_ALL:
    return cities[last][0] or INF

  if dp[last][visited] is not None:
    return dp[last][visited]

  tmp = INF
  for city in range(n):
    if visited & (1 << city) == 0 and cities[last][city] != 0:
      tmp = min(tmp, find_path(city, visited | (1 << city)) * cities[last][city])
  dp[last][visited] = tmp
  return tmp

print(find_path(0, 1 << 0))