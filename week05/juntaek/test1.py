# 비밀번호 4자리 소수
# 비밀번호를 한 번에 한 자리 밖에 못 바꾼다.
# 네 자리 소수 두 개를 입력받아서 바꾸는데 몇 단계나 필요한지 계산!
# 입력은 항상 네 자리 소수만 주어짐. (1000이상)
# A에서 B로 바꾸는 과정에서도 항상 네자리 소수 유지
# 0039 같은 비밀번호 허용 x

 # 일단 해당 넘버가 소수임을 판단하는 함수를 하나 만들어야 할듯
  # 숫자를 하나씩 다 돌면서 숫자를 바꿔바
  # 이때 맨 첫번째 자리는 1이상이어야 함.

import sys

def sosu(number):
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

def change_digit_and_check_prime(n, idx, new_digit):
    n_list = list(str(n))
    n_list[idx] = str(new_digit)
    new_number = int(''.join(n_list))
    return new_number if sosu(new_number) else None

t = int(input())
for _ in range(t):
  n, m = map(int, sys.stdin.readline().split())
  count = 0
  while(n != m):
    list_n = list(map(int, str(n)))

    for i in range(list_n.length()):
      for num in range(0, 10):
        if num == list_n[i]:
          continue
        result = change_digit_and_check_prime(n, i, num)
        if (result > 1000):
          n = max(result, n)
    count +=1

  print('n', n)
  print('m', m)

