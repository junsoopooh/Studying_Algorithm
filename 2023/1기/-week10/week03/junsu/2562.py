import sys
nums = []
for _ in range(9):
    num = int(sys.stdin.readline())
    nums.append(num)

val = max(nums)

ans = nums.index(val)
print(val)
print(ans+1)
