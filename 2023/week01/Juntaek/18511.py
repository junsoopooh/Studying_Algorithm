# input으로 받은 k를 내림차순 정렬해
# 그리고 n을 슬라이싱해서 하나하나 k의 최대값과 비교를 하는거야
# 만약에 k가 n슬라이싱 한 것 보다 하나라도 더 크면 그거는 첫번째 숫자로 사용 불가
# n이랑 비교했는데 k가 다 작다? 그럼 첫번째 숫자로 사용가능
# 그리고 나서는 k에서 최대값 다 붙여버려.
# n, k = map(int, input().split())
# k_list = list(map(int, input().split(' ')))
# k_list.sort(reverse=True)
# print(k_list)

# n_list = list(str(n))
# print(n_list)

# for _ in range(k):
#     for i in range(len(n_list)):
#         if k_list[i] < n_list[i]:
#             tm

from itertools import product
n, m = map(int, input().split())
k = list(map(int, input().split()))
k.sort(reverse=True)
length = len(str(n))

while 1:
    num = list(product(k, repeat=length))
    print(num)
    for a in num:
        a_num = int(''.join(map(str, a)))
        print(a_num)
        if a_num <= n:
            print(a_num)
            exit()
    length -= 1



# 재귀 #
def sol(order, num):
    global final_ans

    if order == len(str(N)): 
        if not '0' in str(num): # K의 원소는 1~9 자연수이므로 0이 들어간 건 안됨
            final_ans = max(final_ans, num) 
        return

    for i in range(K): # K의 원소가 그 자릿수에 들어갈 수 있는지 살펴보기(큰 자릿수부터 채움)
        now_num = arr[i]*(10**(len(str(N))-order-1)) + num

        if now_num <= N: # now_num이 N 이하인 경우
            sol(order + 1, now_num)

        else: # now_num이 N보다 크면
            sol(order+1, num)


N, K = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True) # 큰 수부터 넣어보려고

final_ans= 0
sol(0, 0) # 자릿수 몇번째인지, 그때까지 만든 숫자

# print(ans_list)
print(final_ans)