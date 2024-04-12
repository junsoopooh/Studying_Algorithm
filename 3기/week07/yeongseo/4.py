import math

def solution(numbers):
    def is_prime(num):
        if num <= 1:
            return False 
        
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
            
        return True 
    
    visited = [0] * len(numbers)
    ans = set()
    
    def dfs(part):
        if part != "" and is_prime(int(part)):
            ans.add(part)
        
        for i in range(len(numbers)):
            if not visited[i] and not(len(part) == 0 and numbers[i] == "0"):
                visited[i] = True
                dfs(part + numbers[i])
                visited[i] = False
     
    dfs("")
    return len(ans)