# 소수경로
import sys
from collections import deque
from heapq import heappop, heappush

def check(k:int):
    if not k%2:
        return False
    for i in range(3,int(k**(0.5))+1):
        if not k%i:
            return False
    else:
        return True
    
def change(nums: list):
    result = []
    tmp1 = nums
    tmp2 = nums
    tmp3 = nums
    tmp4 = nums
    for i in range(10):
        tmp1[0] = str(i)
        tmp1_num = int(''.join(tmp1))
        if check(tmp1_num) and tmp1_num >= 1000:
            result.append(tmp1_num)
        
        tmp2[0] = str(i)
        tmp2_num = int(''.join(tmp2))
        if check(tmp2_num) and tmp2_num >= 1000:
            result.append(tmp2_num)

        tmp3[0] = str(i)
        tmp3_num = int(''.join(tmp3))
        if check(tmp3_num) and tmp3_num >= 1000:
            result.append(tmp3_num)

        tmp4[0] = str(i)
        tmp4_num = int(''.join(tmp4))
        if check(tmp4_num) and tmp4_num >= 1000:
            result.append(tmp4_num)
    return result


t = int(sys.stdin.readline())
for _ in range(t):
    answer = 'Impossible'
    a,b = map(int,sys.stdin.readline().split())
    # cnt = 0
    # a_arr = list(str(a))
    # b_arr = list(str(b))
    # new_a_arr = list(str(a))
    # while new_a_arr != b_arr or not limit:
    #     limit -= 1
    #     for i in range(4):
    #         new_a_arr[i] = b_arr[i]
    #         new_a = int(''.join(new_a_arr))
    #         if not check(new_a) or new_a < 1000:
    #             new_a_arr[i] = a_arr[i]
    #         cnt += 1
    # if not limit:
    #     print('Impossible')
    # else:
    #     print(cnt)

    q = deque
    a_arr = list(str(a))
    b_arr = list(str(a))
    heappush(q,[0,a_arr])
    while q:
        cnt, now = heappop(q)
        if now == b_arr:
            answer = cnt
            break        
        arr = change(now)
        for num in arr:
            heappush(q,[cnt+1, num])
    print(answer)