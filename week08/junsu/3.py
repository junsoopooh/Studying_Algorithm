# [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578)

def solution(clothes):
    answer = 0
    arr = dict()
    for x in clothes:
        [n,t] = x
        if t in arr:
            arr[t] += 1
        else:
            arr[t] = 1
    cnt = 1
    for a,b in arr.items():
        cnt *= (b+1)
    # 아무것도 안입은 경우 제외
    answer = cnt-1
    return answer