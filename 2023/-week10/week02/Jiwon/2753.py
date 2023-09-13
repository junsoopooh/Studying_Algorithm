import sys
input = sys.stdin.readline

# 윤년이면 1, 아니면 0

n = int(input())
 
if ((n % 4 == 0) & (n % 100 != 0)) | (n % 400 == 0):
    print(1)
else:
    print(0)