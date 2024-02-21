import sys
input = sys.stdin.readline

# month, date
month, date = map(int, input().split())

dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

day = (sum(dates[0:month]) + date) % 7
print(days[day])