def solution(arr):
    answer = [0, 0]

    def change(a, b, n):
        if n == 1:
            idx = arr[a][b]
            answer[idx] += 1
            return
        else:
            val = arr[a][b]
            for i in range(a, a+n):
                for j in range(b, b+n):
                    if arr[i][j] != val:
                        x1, y1 = a, b
                        x2, y2 = a+n//2, b+0
                        x3, y3 = a+0, b+n//2
                        x4, y4 = a+n//2, b+n//2
                        change(x1, y2, n//2)
                        change(x2, y2, n//2)
                        change(x3, y3, n//2)
                        change(x4, y4, n//2)
                        return
            idx = val
            answer[idx] += 1
            return
    change(0, 0, len(arr))
    return answer
