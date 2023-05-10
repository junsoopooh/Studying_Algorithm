import itertools
# import sys
# input = sys.stdin.readline
# 인풋 받기
N, M = map(int, input().split(' '))
card_list = list(map(int, input().split(' ')))
# print(card_list)
# 5개 중에서 3개 뽑는 방법 순서 고려하지 않고 => 조합
nCr = itertools.combinations(card_list, 3)
# print(nCr)
final_list = []
# 뽑은 게 21보다 작거나 같으면 다른 리스트에 따로 분류
for i in nCr:
    # print(i)
    if sum(i) <= M:
        final_list.append(sum(i))
print(max(final_list))
# 21보다 작은 리스트 중에서 합이 가장 큰 리스트 뽑아
# max_value = sum(final_list[0])
# for i in final_list:
#     if sum(i) > max_value:
#         max_value = sum(i)
# print(max_value)
