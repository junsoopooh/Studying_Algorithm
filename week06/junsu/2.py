# 바탕화면 정리
def solution(wallpaper):
    answer = []
    files_x = []
    files_y = []
    n = len(wallpaper)
    m = len(wallpaper[0])
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                files_x.append(i)
                files_y.append(j)
    answer.append(min(files_x))
    answer.append(min(files_y))
    answer.append(max(files_x)+1)
    answer.append(max(files_y)+1)
    return answer