# a, b, v = map(int, input().split())
# day = 0
# cnt = 0
# while (v-a) > day:
#     day += (a-b)
#     cnt += 1
# print(cnt + 1)

import math
a, b, v = map(int, input().split())
day = math.ceil((v-a)/(a-b)) + 1
print(day)