N = int(input())
sosu_list = list(map(int, input().split()))
not_sosu_list = list()
# print(sosu_list)
cnt = 0
for sosu in sosu_list:
    if sosu == 1:
      not_sosu_list.append(sosu)
    else:
      for i in range(2, sosu):
          if (sosu % i == 0):
              not_sosu_list.append(sosu)
              break
# print(n_sosu)
print(len(sosu_list) - len(not_sosu_list))