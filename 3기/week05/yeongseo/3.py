import math
from collections import deque

test_case_number = int(input())


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    
    return True

def bfs(start, end):
    que = deque([[start, 0]]) # 현재 숫자, 바뀐 횟수
    visited = [0 for _ in range(10001)] # 방문 정보 배열
    visited[start] = 1  # 시작 지점 방문처리

    while que: 
        cur_num, cur_cnt = que.pop() 
        if cur_num == end: # 종료조건
            return cur_cnt 
        
        str_cur_num = list(str(cur_num))
        for n in range(len(str_cur_num)):
            origin = str_cur_num[n] # 한자리씩 바꿀거, 원래 자릿값 기록해둠
            for i in range(0, 10): 
                str_cur_num[n] = str(i)
                changed_cur_num = int(''.join(str_cur_num)) # 한자리 바꿈

                if changed_cur_num >= 1000 and changed_cur_num < 10000 and not visited[changed_cur_num] and is_prime(changed_cur_num) == True: # 한자리 바꿔보고, 그게 소수인지 파악
                    que.appendleft([changed_cur_num, cur_cnt + 1])
                    visited[changed_cur_num] = 1
                
            str_cur_num[n] = origin
    
    return -1


nums = []
for _ in range(test_case_number):
    start, end = map(int, input().split())
    nums.append((start, end))

for start, end in nums:
    ans = bfs(start, end) 

    if ans == -1:
        print("impossible")
    else:
        print(ans)

