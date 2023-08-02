import sys

n,k = map(int,sys.stdin.readline().split())
num = sys.stdin.readline().rstrip()
stk = []

for i in range(n):
    while k > 0 and stk and stk[-1] < num[i]:
        stk.pop()
        k -= 1
    stk.append(num[i])

# k가 0보다 크다 위 while문의 조건을 통해 내림차순으로 정렬되어있어서 계속 추가되었음을 알수있다. 따라서 맨뒤부터 빼면 가장작은수부터 뺄수있음.
if k > 0:
    while k >0:
        stk.pop()
        k -= 1

if k == 0 :
    print(*stk,sep='')