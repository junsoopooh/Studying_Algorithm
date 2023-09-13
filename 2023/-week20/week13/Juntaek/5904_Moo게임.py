# s = []
# def moo(k):
#   if k == 0:
#     return "moo"
#   else:
#     return moo(k-1) + "m" + "o"*(k+2) + moo(k-1)
# print(moo(2))

import sys
input = sys.stdin.readline

s0 = ['m', 'o', 'o']

def bt(n, depth, b_len):
  new_len = 2 * b_len + depth + 3
  if n <= 3:
    print(s0[n - 1])
    return

  if new_len < n:
    bt(n, depth + 1, new_len)
  else:
    if b_len < n and n <= b_len + depth + 3:
      if n - b_len != 1:
        print('o')
      else:
        print('m')
    else:
      bt(n - (b_len + depth + 3), 1, 3)

n = int(input().rstrip())
bt(n, 1, 3)