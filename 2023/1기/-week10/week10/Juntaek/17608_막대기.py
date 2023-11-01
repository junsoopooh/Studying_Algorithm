# 보고 있는 막대기가 기준 막대기 보다 작으면 그냥 count + 1하고 만약 기준 막대기 보다 높으면? 기준 막대기 업데이트까지?
# 아니다 그냥 일단 리스트에 들어간 막대기랑만 비교를 하면 되잖아? 맨처음에만 기준 막대기랑 비교하고 그 이후부터는 리스트에 들어간 막대기랑만 비교하면 될듯?
import sys
input = sys.stdin.readline
n = int(input())
bar_list = []
for _ in range(n):
    bar_list.append(int(input()))
# print(bar_list)

count = 1
key = len(bar_list)-1
for i in range(len(bar_list)-2, -1, -1):
    if bar_list[i] > bar_list[key]:
        key = i
        count += 1
print(count)