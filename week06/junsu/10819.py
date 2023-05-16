import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

nums.sort()
ans = 0
if n%2 == 0:
    for i in range(n):
        if i%2 == 0:
            min_val = min(nums[i:])
            min_index = nums.index(min_val)
            nums[min_index] = nums[i]
            nums[i] = min_val
        else:
            max_val = max(nums[i:])
            max_index = nums.index(max_val)
            nums[max_index] = nums[i]
            nums[i] = max_val
else:
    mid_index = (n//2)+1
    mid = nums[mid_index]
    pref = mid - nums[mid_index-1]
    next = nums[mid_index+1] - mid
    if max < min: # 중간값이 최저와 가까우니 가장 먼저 최솟값이 와야함
        for i in range(n):
            if i%2 == 0:
                min_val = min(nums[i:])
                min_index = nums.index(min_val)
                nums[min_index] = nums[i]
                nums[i] = min_val
            else:
                max_val = max(nums[i:])
                max_index = nums.index(max_val)
                nums[max_index] = nums[i]
                nums[i] = max_val
    else:
        for i in range(n):
            if i%2 == 0:
                max_val = max(nums[i:])
                max_index = nums.index(max_val)
                nums[max_index] = nums[i]
                nums[i] = max_val
            else:
                min_val = min(nums[i:])
                min_index = nums.index(min_val)
                nums[min_index] = nums[i]
                nums[i] = min_val

for i in range(n-1):
    ans += abs(nums[i]-nums[i+1])
print(ans)