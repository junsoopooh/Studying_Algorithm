def solution(n):
    ans = 0 
    
    for i in range(2, n+1):
        if ara(i) == True:
            ans += 1
    
    return ans

def ara(num):
    for i in range(2, int(num ** 0.5) + 1): # 2 ~ root(숫자) 까지 에라토스테네스의체
        if num % i == 0:
            return False 
    
    return True
    