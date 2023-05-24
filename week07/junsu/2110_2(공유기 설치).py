import sys

house = []
n,c = map(int,sys.stdin.readline().split())
for _ in range(n):
    house.append(int(sys.stdin.readline()))

house.sort()

distance = house[-1]-house[0]
max_val = distance // c
left = house[1]-house[0]
right = max_val
while left <= right:
        mid = (left + right)//2
        for i in range(n-1):
            if house[i+1]-house[i]>mid:
                 left = mid + 1
                 break
            
            ans = max(mid,max_val)
print(ans)