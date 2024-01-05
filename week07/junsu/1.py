# 약수의 합
def solution(n):
    answer = 0
    for i in range(1,int(n**(0.5))+1):
        if not n%i:
            answer += (i+n//i)
            if i == n//i:
                answer -= i    
    return answer