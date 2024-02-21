id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]

report = list(set(report))

k = 3
answer = dict()
for i in id_list:
    answer[i] = 0

# 신고 당한 횟수 저장
for i in range(len(report)):
    tmp = report[i].split(" ")
    answer[tmp[1]] += 1

# 신고당한 횟수가 k 이상인 친구들을 모아두기 위한 리스트
singoList = []

# 신고당한 횟수가 k 이상인 친구들을 찾기 위한 반복문
for key,value in zip(answer.keys(),answer.values()):
    if value >= k:
        singoList.append(key)

# 다시한번 dictionary 초기화 -> 최종적으로 신고했던 친구들의 횟수들을 올리기위해
answer = dict()
for i in id_list:
    answer[i] = 0

# singoList를 활용해 신고 횟수가 K이상인 친구들 ++
for i in range(len(report)):
    tmp = report[i].split(" ")
    if tmp[1] in singoList:
        answer[tmp[0]] += 1

# 최종적으로 답을 return 하기위한 List 변환과정
result = []
for i in answer.values():
    result.append(i)
print(result)




