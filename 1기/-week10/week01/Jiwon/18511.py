import sys
input = sys.stdin.readline

def makeNum(length, num):
    global result

    if length == len(str(n)): 
        if not '0' in str(num):
            result = max(result, num) 
        return

    for i in range(k):
        temp = 10 ** (len(str(n))-length-1)
        now_num = numbers[i] * temp + num

        if now_num <= n:
            makeNum(length+1, now_num)
        else:
            makeNum(length+1, num)

# 자연수 n, 집합 numbers의 원소 개수 k
n, k = map(int, input().split())

# 원소 집합 numbers
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

# 리턴 변수
result = 0

makeNum(0, 0)

print(result)