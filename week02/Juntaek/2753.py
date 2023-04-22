# 4의 배수이면서 100의 배수가 아닐 때 or 400의 배수일 때
year = int(input())
if (year%400 == 0) or (year%4 == 0) and ((year%100 != 0)):
    print(1)
else:
    print(0)

print('1') if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0) else print('0')