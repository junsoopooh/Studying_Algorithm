import sys

champs = []
n,k = map(int,sys.stdin.readline().split())
for _ in range(n):
    champs.append(int(sys.stdin.readline()))

champs.sort()
left = champs[0]
right = champs[-1] + k
ans = []

while left<=right:
    mid = (left + right) // 2
    tmp = 0
    for i in champs:
        if i < mid:
            tmp += mid-i
    if tmp <= k:
        ans.append(mid)
        left = mid +1
    else:
        right = mid -1

print(max(ans))