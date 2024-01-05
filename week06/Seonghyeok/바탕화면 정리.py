'''
1. 가장 큰 (x,y) 값과 가장 작은 (x,y) 구함
2. 큰 값은 += 1 작은 값은 그대로
'''
def solution(wallpaper):
    answer = []
    row = []
    column = []
    for idx,w in enumerate(wallpaper):
        lst = list(w)
        for idx_lst,j in enumerate(lst):
            if j == '#':
                row.append(idx)
                column.append(idx_lst)

    answer.append(min(row))
    answer.append(min(column))
    answer.append(max(row)+1)
    answer.append(max(column)+1)


    return answer










print(solution(["..", "#."]))
# -> [0, 1, 3, 4]