import sys

nums = sys.stdin.readline().rstrip().split('-')
ans = 0
for i in nums[0].split('+'):
    ans += int(i)

for i in nums[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)
