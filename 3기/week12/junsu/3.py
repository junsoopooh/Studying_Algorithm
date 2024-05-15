# [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747)

def solution(citations):
    answer = 0
    left = 0
    right = 10000
    while left <= right:
        cnt = 0
        mid = (left+right)//2
        for i in citations:
            if i >= mid:
                cnt += 1
        if cnt < mid:
            right = mid -1
        else:
            left = mid +1
            
    answer = (left+right)//2 
    return answer