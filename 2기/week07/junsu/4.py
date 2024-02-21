# 줄 서는 방법

import math

def solution(n, k):
    answer = []
    arr = list(range(1,n+1))
    while n>0:
        tmp = math.factorial(n-1)
        a = k//tmp
        k = k%tmp
        if k:
            answer.append(arr[a])
            arr.pop(a)
        else:
            answer.append(arr[a-1])
            arr.pop(a-1)
        n -= 1
    return answer