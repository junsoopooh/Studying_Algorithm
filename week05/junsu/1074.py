import sys

n,r,c = map(int,sys.stdin.readline().split()) # 2**n가 크기, r : 행, c : 열


def search(n,r,c,ans):
    if n == 0:
        print(ans)
        return
    length = 2**n 
    if r < 2**(n-1) and c < length//2: #4등분 기준 왼쪽 위에 있음
        search(n-1,r,c,ans)
    elif r >= length//2 and c < length//2: # 왼쪽 아래
        search(n-1,r-2**(n-1),c,ans+(length**2)//2)
    elif r < length//2 and c >= length//2: # 오른쪽 위
        search(n-1,r,c-2**(n-1),ans+(length**2)//4)
    elif r >= length//2 and c >= length//2:                               # 오른쪽 아래
        search(n-1,r-2**(n-1),c-2**(n-1),ans+3*(length**2)//4)

search(n,r,c,0)
