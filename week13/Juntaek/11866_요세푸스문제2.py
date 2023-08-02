from collections import deque
n, k = map(int, input().split())
list = deque(i for i in range(1, n+1))
new_list = []
print(list)
while len(list) > 0:
  for _ in range(k-1):
    list.append(list.popleft())
  new_list.append(str(list.popleft()))
# print(new_list)
print("<" + ", ".join(new_list) + ">")