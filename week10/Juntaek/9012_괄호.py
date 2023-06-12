# 괄호 모양이 올바르게 구성 : VPS
n = int(input())
for _ in range(n):
    data = input()
    # print(data)
    is_vps = []
    for i in data:
        if len(is_vps) == 0:
            if i == '(':
                is_vps.append(i)
            else:
                print('NO')
                break
        else:
            if is_vps[-1] == '(':
                if i == '(':
                    is_vps.append(i)
                else:
                    is_vps.pop()
            else:
                print('NO')
                break
    else: 
      if len(is_vps) == 0:
          print('YES')
      else:
          print('NO')