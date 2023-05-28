import sys

m,n,l = map(int,sys.stdin.readline().split()) # 사대의 수, 동물의 수, 사정거리
shots = list(map(int,sys.stdin.readline().split())) # 사대 좌표
shots.sort()
targets = []
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    targets.append([x,y])

cnt = 0
for animal in targets:
    x = animal[0]
    y = animal[1]
    left = 0
    right = m-1
    while left <= right:
        mid = (left + right) //2
        if abs(shots[mid]-x)+y <= l:
            cnt += 1
            break
        else:
            if shots[mid] <= x:
                left = mid +1
            else:
                right = mid -1

print(cnt)