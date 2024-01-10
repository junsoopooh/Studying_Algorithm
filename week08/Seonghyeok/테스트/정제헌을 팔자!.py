'''
1.회사에서 사용하는 모든 플라스크 및 비커의 용량은 전부 1/n (n은 자연수) 꼴이여야 한다
2.판매 및 보관를 위한 모든 약은 플라스크 및 비커에 가득 담겨져 있어야한다

2 -> 4 4
4 -> 8 8
1 -> 2 2
=> *2배씩

n = (xy)/(x+y)
'''

for _ in range(4):
    n = input()
    answer = 0
    num = n.split('/')
    val = int(num[1])
    for i in range(1,(val*2)+1):
        for j in range(1,(val*2)+1):
            if val == (i*j)/(i+j):
                answer += 1
    print(answer)

