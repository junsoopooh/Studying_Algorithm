import itertools
# 일단 난쟁이를 리스트에 넣자
nan_list = [int(input()) for _ in range(9)]
nan_list.sort()
# print(nan_list)
# 난쟁이 리스트안에 9명 중 7명을 뽑아서 그것의 합이 100이면 그때 7명의 난쟁이를 찾음!
nCr = itertools.combinations(nan_list, 7)
for i in nCr:
    if sum(i) == 100:
        ret = i
for i in ret:
    print(i)
# print(list(nCr))


### 다시 풀어보기 ###
import itertools
nanjang  = [int(input()) for _ in range(9)]
nanjang.sort()
real_list = []
print(nanjang)
nCr = itertools.combinations(nanjang, 7)
for i in nCr:
    if sum(i) == 100:
        real_list.append(i)
        print(real_list)
real_list = str(real_list)[1:-1]
print(real_list)
real_a = list(real_list)
print(real_a)
# print(real_list)
# for i in real_list:
#     print(i)