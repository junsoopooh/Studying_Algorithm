import sys
input = sys.stdin.readline
M, N, L = map(int, input().split())
shots_place = list(map(int, input().split()))
animals_place = []
for i in range(N):
    a, b = map(int, input().split())
    animals_place.append((a, b))

answer = 0
shots_place.sort()
for a, b in animals_place:
    start, end = 0, len(shots_place)-1
    mid = 0
    while start < end:
        mid = (start+end)//2
        if shots_place[mid] < a:
            start = mid + 1
        elif shots_place[mid] > a:
            end = mid - 1
        else:
            start = mid
            break
    if abs(shots_place[start]-a)+b <= L:
        answer += 1
    elif start+1 < len(shots_place) and abs(shots_place[start+1]-a)+b <= L:
        answer += 1
    elif start > 0 and abs(shots_place[start-1]-a)+b <= L:
        answer += 1
print(answer)
    