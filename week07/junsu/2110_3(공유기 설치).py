import sys

n, c = map(int, sys.stdin.readline().split())
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline()))

houses.sort()

if c == 2:
    print(houses[-1]-houses[0])
else:
    left = 0
    right = houses[-1]-houses[0]
    ans = []
    while left <= right:
        mid = (left + right)//2
        last = houses[0]
        cnt = 1
        for i in range(1, n):
            if houses[i]-last >= mid:
                cnt += 1
                last = houses[i]
        if cnt < c:
            right = mid - 1
        elif cnt >= c:
            ans.append(mid)
            left = mid + 1
    
    print(max(ans))
