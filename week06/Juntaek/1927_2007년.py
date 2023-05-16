x, y = map(int, input().split())
day_num = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day_sum = 0


for i in range(x):
    day_sum += day_num[i]
# print(day_sum)

total = (day_sum + y) % 7
# print(total)
print(day[total])
