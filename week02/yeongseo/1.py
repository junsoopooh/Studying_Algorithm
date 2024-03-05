def solution(x):
    nums = []
    
    origin_x = x
    while x > 0:
        nums.append(x % 10)
        x = x // 10
    
    if origin_x % sum(nums) == 0:
        return True
    else:
        return False