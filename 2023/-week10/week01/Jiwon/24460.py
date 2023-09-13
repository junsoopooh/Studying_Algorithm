import sys
input = sys.stdin.readline

# 네 부분으로 분리하여 재귀 타기
def getSecond(size, x, y):
    if size == 1:
        return chairs[x][y]
    
    else:
        scores = [getSecond(size//2, x, y),
                  getSecond(size//2, x, y + size//2),
                  getSecond(size//2, x + size//2, y),
                  getSecond(size//2, x + size//2, y + size//2)]
        
        scores.sort()

        # 두번째 순위 가져오기
        return scores[1]

n = int(input())
chairs = [list(map(int, input().split())) for _ in range(n)]

print(getSecond(n, 0, 0))