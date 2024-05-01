#[메뉴 리뉴얼](https://school.programmers.co.kr/learn/courses/30/lessons/72411)

# 1차시도 85/100
import itertools

def solution(orders, course):
    answer = []
    arr_set = set()
    for i in range(len(orders)):
        for j in range(len(orders[i])):
            arr_set.add(orders[i][j])
        orders[i] = set(orders[i])
        
    for n in course:
        arr = []
        cnt = 2
        nCr = itertools.combinations(arr_set,n)
        for x in list(nCr):
            tmp = 0
            for p in orders:
                if set(x) <= p:
                    tmp += 1
            k = sorted(x)
            word = ''.join(k)
            if tmp > cnt:
                cnt = tmp
                arr = [word]
            elif tmp == cnt:
                arr.append(word)
        answer += arr
    answer.sort()
    return answer


# 2차 시도 100/100
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for n in course:
        arr = []
        for order in orders:
            for x in combinations(order, n):
                word = ''.join(sorted(x))
                arr.append(word)
        sorted_arr = Counter(arr).most_common()
        for menu, cnt in sorted_arr:
            if cnt > 1 and cnt == sorted_arr[0][1]:
                answer.append(menu)
    answer.sort()
    return sorted(answer)