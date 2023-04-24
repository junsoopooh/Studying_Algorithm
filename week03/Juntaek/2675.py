T = int(input())
for _ in range(T):
    data = input().split()
    # print(data)
    R = int(data[0])
    S = data[1]
    for i in S:
      print(i * R, end='')
    print()