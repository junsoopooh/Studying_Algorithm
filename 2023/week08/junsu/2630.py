import sys

n = int(sys.stdin.readline())

matrix = []
for _ in range(n):
    col = list(map(int,sys.stdin.readline().split()))
    matrix.append(col)

w_cnt = 0
b_cnt = 0 # 파란색 색종이

def cut(a,b,k):
    global w_cnt,b_cnt
    color = matrix[a][b]
    if k == 1:
        if color == 1:
            b_cnt += 1
            return
        else:
            w_cnt += 1
            return
    
    
    for x in range(a,a+k):
        for y in range(b,b+k):
            if matrix[x][y] != color:
                cut(a,b,k//2)
                cut(a+k//2,b,k//2)
                cut(a,b+k//2,k//2)
                cut(a+k//2,b+k//2,k//2)
                return
    
    if color == 1:
        b_cnt += 1
        return
    else:
        w_cnt += 1
        return

cut(0,0,n)

print(w_cnt)
print(b_cnt)
