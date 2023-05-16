# 순열 사용해서 배열의 순서를 하나하나 다 따져
import itertools
n = int(input())
A = list(map(int, input().split()))
sum_list = []
# print(A)
nPr = itertools.permutations(A)
# print(list(nPr))
for i in nPr:
    ret = []
    for j in range(len(i)-1):
        ret.append(abs(i[j]- i[j+1]))
        # print(ret)
    sum_list.append(sum(ret))
print(max(sum_list))
      