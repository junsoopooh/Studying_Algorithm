import sys

n = int(sys.stdin.readline())
solution = list(map(int,sys.stdin.readline().split()))

solution.sort()
left = 0
right = n-1
min_val = 10**10
ans = [0,0]
while left<right:
    tmp = solution[left] + solution[right]
    if abs(tmp)<abs(min_val):
        min_val = tmp
        ans[0] = solution[left]
        ans[1] = solution[right]
    if tmp == 0:
        break
    if tmp >= 0:
        right -= 1 
    else:
        left += 1

print(*ans)
