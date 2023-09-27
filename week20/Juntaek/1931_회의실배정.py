import sys
input = sys.stdin.readline
n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
# print(meeting)
# meeting.sort(key=lambda x: (x[0], x[1]))
sorted_time = sorted(meeting, key = lambda x : (x[1], x[0]))

# print(sorted_time)
top = 0
cnt = 0
for time in sorted_time:
  if time[0] >= top:
    top = time[1]
    cnt += 1
print(cnt)