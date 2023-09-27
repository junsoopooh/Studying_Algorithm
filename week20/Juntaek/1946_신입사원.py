# 1차 서류 2차 면접 점수 존재
# 참가자의 서류, 면접 점수가 다른 참가자들보다 모두 뒤떨어지면 안뽑아
# 위 조건 만족시키면서, 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램!
# 입력으로는 지원자의 각각 서류 면접 순위가 주어진다
# 일단 n이 결국 최하 등수임
# 서류 점수가 1등이야 그러면 면접은 볼 필요도 없이 얘는 통과
# 만약이 서류 점수 2등이야 그러면 서류 3등인 지원자의 면접점수는 볼 필요가 없어 어차피 서류점수가 얘들 보다 높으니까 근데 만약 1등이랑 면접 점수 비교했는데 등수가 더 낮다? 얘는 탈락
# 서류 기준 오름차순 정렬 해서 2등부터 자신 보다 서류 등수가 높은 친구의 면접 점수를 비교한 후 만약 면접 점수도 더 낮다면 얘는 탈락시키는 방법 혹은 면접 점수가 더 높으면 answer에 정답을 넣는 방법
# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#   n = int(input())
#   man_list = []
#   answer = []
#   for _ in range(n):
#     man_list.append(list(map(int, input().split())))
#     # print(man_list)
#   man_list.sort()
#   # print(man_list)
#   answer.append(man_list[0])
#   # print(man_list)
#   for i in range(1, len(man_list)):
#     for j in range(i-1, -1, -1):
#       if man_list[i][1] < man_list[j][1]:
#         answer.append(man_list[i])
#         # print(answer)
#         break
#       else:
#         break
#   print(len(answer))

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  rank_list = [list(map(int, input().split())) for _ in range(n)]
  rank_list.sort()

  top = rank_list[0][1]
  cnt = 1

  for rank in rank_list:
    if rank[1] < top:
      top = rank[1]
      cnt += 1
  print(cnt)