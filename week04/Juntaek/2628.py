# row, col = map(int, input().split())
# print(row, col)
# jongeee = [(0 * row) for _ in range(col) ]
# print(jongeee)
# # 1. 배열 만들기
# # 2. 어떻게 할까? 일단 잘라야 돼..
# # 음.. 배열이 있으면 입력을 받은 대로 하나하나 일단 잘라야 돼.
# # 자르고 나서 가장 큰 넓이를 구해야지?
# r, c = map(int, input().split())
# # 자르는 위치 저장
# row = [0, r]
# column = [0, c]

# for _ in range(int(input())):
#     r_or_c, linenumber = map(int, input().split())
#     if r_or_c == 1:
#         row.append(linenumber)
#     else:
#         column.append(linenumber)
# row.sort()
# column.sort()

# subtracted_r = []
# subtracted_c = []

# for i in range(len(row) - 1):
#     subtracted_r.append(row[i + 1] - row[i])
# for i in range(len(column) - 1):
#     subtracted_c.append(column[i+1] - column[i])
# print(max(subtracted_r) * max(subtracted_c))

### 다시 구현해보기 ####
r, c = map(int, input().split())
row = [0, r]
column = [0, c]
for _ in range(int(input())):
    r_or_c, line = map(int, input().split())
    if r_or_c == 1:
        row.append(line)
    else:
        column.append(line)
row.sort()
column.sort()
sub_r = []
sub_c = []
for i in range(len(row)):
    sub_r.append(row[i]-row[i-1])
for i in range(len(column)):
    sub_c.append(column[i]-column[i-1])
print(max(sub_r) * max(sub_c))