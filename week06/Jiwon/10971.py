import sys
input = sys.stdin.readline

total = sys.maxsize

n = int(input())
values = [list(map(int, input().split())) for _ in range(n)]

def city(start, next, value, visited):
    global total

    # 초반에 탈출 조건이 나와야
    if n == len(visited):
        # 마지막 도시에서 돌아올 수 있다면,
        if values[next][start] != 0:
            total = min(total, values[next][start] + value)
        return

    for i in range(n):
        # value < total: 다음 도시로 가는 비용이 현재 총합보다 크다면 갈 필요 없음
        if values[next][i] != 0 and i not in visited and value < total:
            visited.append(i)
            city(start, i, values[next][i] + value, visited)
            visited.pop()

for i in range(n):
    city(i, i, 0, [i])

print(total)