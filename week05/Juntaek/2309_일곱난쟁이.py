import itertools
# 일단 난쟁이를 리스트에 넣자
nan_list = [int(input()) for _ in range(9)]
nan_list.sort()
# print(nan_list)
nCr = itertools.combinations(nan_list, 7)
for i in nCr:
    if sum(i) == 100:
        ret = i
for i in ret:
    print(i)
# print(list(nCr))
# 난쟁이 리스트안에 9명 중 7명을 뽑아서 그것의 합이 100이면 그때 7명의 난쟁이를 찾음!
