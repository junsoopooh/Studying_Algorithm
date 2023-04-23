num_list = [int(input()) for i in range(9)]
# max() 최댓값 찾기
max_num = max(num_list)
# print(max_num)

# num_list에서 최댓값의 인덱스 찾기
for i in range(len(num_list)):
    if num_list[i] == max_num:
        max_index = i
        break
print(max_num)
print(max_index + 1)