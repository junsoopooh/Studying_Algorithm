import sys

n,c = map(int,sys.stdin.readline().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()
left = n-1
right = 1
location = house[0]
max_val = 1

while left<=right:
    mid = (left+right)//2
    distance = house[mid]-house[0]
    while location < house[-1]:
        location += distance
        if location not in house:
            right = mid-1
            break
    if location == house[-1]:
        max_val = max(max_val, mid)
        left = mid +1
print(max_val)