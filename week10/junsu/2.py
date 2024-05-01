#[소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/12921)

def solution(n):
    answer = 0
    for num in range(2,n+1):
        if num == 2 or num == 3:
            answer += 1
            continue
        if not num%2:
            continue
        for i in range(2,int(num**(0.5))+1):
            if not num%i:
                break
        else:
            answer += 1
    return answer