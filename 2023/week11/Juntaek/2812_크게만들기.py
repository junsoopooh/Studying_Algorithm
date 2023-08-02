# N자리수에서 K를 지운다.
# 그럼 오름차순 정렬 시켜놓고 가장 작은 것부터 K만큼 제거
# 이때, 원래의 정렬 순서가 변하면 안되니 sorted로 새로운 배열 생성
# 그리고 나서 새로운 배열과 기존 배열 비교
# 새로운 배열에 있는 원소들만 기존 배열에서 차례대로 추출
# N, K = map(int, input().split())
# # print(N, K)
# num = int(input())
# num_list = list(map(int, str(num)))
# # print(num_list)
# sort_num_list = sorted(num_list, reverse=True)
# new_list = []
# # print(sort_num_list)
# for _ in range(K):
#     a = sort_num_list.pop()
#     new_list.append(a)
# print(new_list)
# # if sort_num_list in num_list:
# a_sub_b = [x for x in num_list if x not in new_list]
# # print(a_sub_b)
# result = ''.join(str(x) for x in a_sub_b)
# print(result)

# 단순히 가장 작은 수부터 빼면 안됨
# 가장 높은 자리수부터 차근차근 다음 자리수랑 비교해가면서
# 만약 가장 높은 자리수가 그 다음 자리수보다 숫자가 작으면 걔를 지워줘야함. (뒤에서 아무리 작은 수 빼봤자 가장 높은 자리수가 낮은 숫자면 의미없음)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
number = input().rstrip()
# print(number)
stack = []
for x in number:
    while stack and stack[-1] < x and k > 0:
        stack.pop()
        k -= 1
    stack.append(x)
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))