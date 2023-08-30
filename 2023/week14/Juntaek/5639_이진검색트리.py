# 이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램

pre = []
while True:
  try:
    pre.append(int(input()))
  except:
    break

def post(start, end):
  if start > end:
    return
  mid = end + 1
  for i in range(start + 1, end + 1):
    if pre[i] > pre[start]:
      mid = i
      break
  post(start + 1, mid - 1)
  post(mid, end)
  print(pre[start])

post(0, len(pre) - 1)