# 재현이가 잘못된 수 외쳐서 0을 외치면 제일 최근 수를 팝 시킨다.
# 0이 아닌 경우 해당 수를 쓴다.
n = int(input())
num_list = []
for _ in range(n):
    num = int(input())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)
print(sum(num_list))