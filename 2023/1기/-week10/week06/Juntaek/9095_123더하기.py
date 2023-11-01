import itertools
t = int(input())
list = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3]
cnt = 0
for _ in range(t):
    n = int(input())
    for i in range(1, n+1):
       perm = set(itertools.permutations(list, i))
       for j in perm:
          #  print(j)
           if sum(j) == n:
               cnt += 1
    print(cnt)