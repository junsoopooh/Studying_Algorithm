# 문자열에서 폭발 문자열의 첫번째 요소가 등장하는 순간 검사 시작
# 파이썬에서는 특정 문자를 기준으로 분할이 가능한걸로 아는데?
# 그러면 폭발 문자열 기준으로 다 분할을 해
# 그리고 나서 다시 이어붙여
# 언제까지? 폭발 문자열이 문자열에 없을 때까지

str_list = input()
bomb = input()

# while 폭발 문자열이 문자열내에 있으면:
#   문자열.split('폭발문자열')
#   "".join(문자열)
while bomb in str_list:
  str_list = str_list.split(bomb)
  # print(new_str_list)
  str_list = "".join(str_list)
  # print(str_list)
if len(str_list) == 0:
    print("FRULA")
else:
  print(str_list)


### stack 이용해서 개선 ###
S = input()
bomb = input()

stack = []
bomb_len = len(bomb)

for i in range(len(S)):
  stack.append(S[i])
  if ''.join(stack[-bomb_len:]) == bomb:
    for _ in range(bomb_len):
      stack.pop()
if stack:
  print("".join(stack))
else:
  print("FRULA")

