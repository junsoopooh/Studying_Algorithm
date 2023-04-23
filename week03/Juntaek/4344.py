n = int(input())
for _ in range(n):
    test_case = list(map(int, input().split()))
    # print(test_case)
    tall_list = []
    student_num = test_case[0]
    student_score_list = test_case[1:]
    score_avg = sum(student_score_list) / student_num
    for score in student_score_list:
        if score > score_avg:
            tall_list.append(score)
    # print(score_avg)
    # print(len(tall_list))
    print(f'{((len(tall_list) / student_num) * 100):.3f}%')