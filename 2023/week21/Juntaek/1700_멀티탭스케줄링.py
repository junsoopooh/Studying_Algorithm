# 사용횟수가 가장 많은 순으로 새로운 리스트에 정렬
# stack에 사용횟수 많은 순으로 n만큼 푸시
# n부터 use_count길이만큼 for문 돌려서
# 만약 stack에 있는 숫자다? 그럼 그냥 continue
# stack에 없는 숫자다? 그러면 stack.pop() 때리고 새로운 숫자 푸시
# 팝할때 cnt += 1
# 하나씩 플러그를 빼는 최소의 횟수를 출력

# n, k = map(int, input().split())
# use_count = list(map(int, input().split()))
# new_list = []
# stack = []
# cnt = 0

# for i in use_count:
#   if i in stack:
#     continue
#   else:
#     stack.append(i)
# # print(stack)
# stack = stack[:n]
# # print(stack)
# for i in range(n, len(use_count)):
#   if use_count[i] in stack:
#     continue
#   else:
#     stack.pop()
#     cnt+=1
#     stack.append(use_count[i])
# print(cnt)
from asyncore import close_all
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
use = list(map(int, input().split()))

plugs = []
result = 0
for i in range(K):
  if use[i] in plugs:
    continue

  if len(plugs) != N:
    plugs.append(use[i])
    continue

  far_one = 0
  temp = 0
  for plug in plugs:
    if plug not in use[i:]:
      temp = plug
      break
    elif use[i:].index(plug) > far_one:
      far_one = use[i:].index(plug)
      temp = plug
  plugs[plugs.index(temp)] = use[i]
  result += 1
print(result)