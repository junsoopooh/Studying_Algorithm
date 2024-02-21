# 124 나라의 숫자

def solution(n):
    nums = []
    while n:
        a = n%3
        if a:
            n = n//3
            nums.append(str(a))
        else:
            n = n//3 -1
            nums.append('4')
    nums.reverse()
    answer = ''.join(nums)        
    return answer