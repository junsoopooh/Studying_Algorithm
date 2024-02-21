a = int(input())
b = int(input())
c = int(input())
num = [0 for _ in range(10)]
ret = a * b * c
ret = str(ret)
for i in ret:
    # print(i)
    i = int(i)
    num[i] += 1
for i in num:
    print(i)