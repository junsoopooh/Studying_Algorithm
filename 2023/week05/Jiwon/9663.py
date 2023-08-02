import sys
input = sys.stdin.readline

n = int(input())

chess = [None] * n
result = 0

def checking(x):
    for i in range(x):
        # 다른 퀸이 같은 열에 있거나, 대각선에 있거나
        # 현재 퀸을 맨 윗 행부터 차례로 채우고 있으므로 왼쪽 위 대각선, 오른쪽 위 대각선만 확인하면 됨 (아래쪽 확인할 필요 X)
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == abs(x-i):
            return False
        
    return True

def queens(x):
    global result

    # 현재 놓는 퀸이 마지막 퀸이라면, + 1
    if n == x:
        result += 1
        return
    
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다는 의미
            chess[x] = i

            if checking(x):
                queens(x+1)

queens(0)

print(result)