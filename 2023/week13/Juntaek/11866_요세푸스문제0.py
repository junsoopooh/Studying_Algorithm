# 1,2,3,4,5,6,7 k번째 사람 제거 (3)
# 1,2,4,5,6,7 (3)
# 1,2,4,5,7 (6)
# 1,4,5,7 (2)
# 1,4,5 (7)
# 1,4 (5)
# 4 (1)
# n명의 사람이 원을 이루면서 앉아있다.
# k번째 사람을 제거하자.
from collections import deque
n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
# queue = [i for i in range(1, n+1)]
# while문을 돌리는데 list안에 숫자가 1개 남을 때까지
# 이때 k번째 숫자를 삭제하고 그때의 인덱스를 기억해
# 다음번에는 그 인덱스-1 + k번째 숫자를 제거해
# while len(queue) != 1:
# k-1번을 popleft후 append하고 k번째 숫자는 popleft후 리스트에 담기
# for i in range(len(queue)):
res = []
for i in range(len(queue)):
  for _ in range(k-1):
    data = queue.popleft()
    queue.append(data)
  res.append(str(queue.popleft()))
print("<" + ', '.join(res) + ">")