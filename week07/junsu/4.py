# [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839)

# 50/100
from itertools import permutations

def check_prime(n):
    if not n%2:
        return False
    for i in range(3,int(n**(0.5)+1)):
        if not n%i:
            return False
    return True

def make_arr(arr):
    result = []
    n = len(arr)
    for i in range(2,n+1):
        tmp = permutations(arr,i)
        result += list(tmp)
    return result + arr
        

def solution(numbers):
    answer = 0
    nums = set()
    arr = list(numbers)
    result = make_arr(arr)
    for i in result:
        tmp = int("".join(i))
        if check_prime(tmp) and tmp not in nums:
            answer += 1
            nums.add(tmp)
    return answer

# 100/100
from itertools import permutations



# 100/100
from itertools import permutations

def check_prime(n):
    if n < 2:
        return False
    elif n<4:
        return True
    
    if not n%2:
        return False
    
    for i in range(2,int(n**(0.5))+1):
        if not n%i:
            return False
    else:
        return True

def make_arr(arr):
    result = []
    n = len(arr)
    tmp = []
    for i in range(1,n+1):
        tmp += list(permutations(arr,i))
    for a in tmp:
        result.append(int("".join(a)))
    return result

def solution(numbers):
    result = set()
    arr = list(numbers)
    arr = make_arr(arr)
    arr = set(arr)
    for i in arr:
        if check_prime(int(i)):
            result.add(int(i))
    return len(result)