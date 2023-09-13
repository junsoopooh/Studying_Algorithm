# 2차원 배열을 통한 정답코드
import sys
n = int(sys.stdin.readline())

row = [[0]*n for i in range(n)]
count = 0

def queen(a):
    
    if a == n:
        global count
        count+=1
        return
    # 퀸이 모두 놓였으므로 카운트하고 종료
    
    for i in range(n):
        skip = 0
        for j in range(n):
            if row[j][i] == 1:
                break
       	# 수직상의 퀸 검사
        else:
            for k in range(a):
                if (row[k].index(1) == i + a-k) | (row[k].index(1) == i - (a-k)): # \ = 둘중 하나라도 1이면 1
                # 대각선상의 퀸 검사
                    skip = 1
                    break
            if skip == 1:
                continue
                # 반복문 두 개를 한번에 건너뛸 수 없으므로
                # 변수를 활용해준다.
            row[a][i] = 1
            queen(a+1)
            row[a][i] = 0
        
queen(0)
print(count)