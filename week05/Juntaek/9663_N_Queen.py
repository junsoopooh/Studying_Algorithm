n = int(input())
n_queen_list = [[0] * n for _ in range(n)]
print(n_queen_list)

### 정답 ###
ans = 0
row = [0] * n
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False

    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)
n_queens(0)
print(ans)
