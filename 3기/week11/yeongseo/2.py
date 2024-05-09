import math
def solution(nums):
    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        
        return True
    
    primes = 0
    def dfs(cur_num, idx):
        nonlocal primes
        if len(cur_num) == 3:
            if is_prime(sum(cur_num)):
                primes += 1
            return
        
        for i in range(idx, len(nums)):
            dfs(cur_num + [nums[i]], i + 1)
    
    dfs([], 0)
    
    return primes
