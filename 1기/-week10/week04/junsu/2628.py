import sys

a,b= map(int,sys.stdin.readline().split()) # 가로,세로
t = int(sys.stdin.readline()) # 잘라야 하는 점선의 갯수
list_ud = []
list_ud.append(b)
list_rl = []
list_rl.append(a)
for _ in range(t):
    p,q=map(int,sys.stdin.readline().split()) # p = 0, 가로로 자르는 점선 

    if p == 0:
        list_ud.append(q)
    else:
        list_rl.append(q)

list_ud.append(0)
list.sort(list_ud)
list_rl.append(0)
list.sort(list_rl)

max_ud=0
max_rl=0
for i in range(len(list_ud)-1):
    tmp = list_ud[i+1]-list_ud[i]
    max_ud = max(tmp,max_ud)

for i in range(len(list_rl)-1):
    tmp = list_rl[i+1]-list_rl[i]
    max_rl = max(tmp,max_rl)

print(max_rl*max_ud)
