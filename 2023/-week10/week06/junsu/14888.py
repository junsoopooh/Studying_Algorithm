import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
plus, minus, multiple, division = map(int,sys.stdin.readline().split())
sign = [plus,minus,multiple,division]
def sum(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if x > 0 and y < 0:
        return x//(-y)*(-1)
    elif x < 0 and y > 0:
        return (-x)//y*(-1)

def calculate(index,ans):
    if index == n-1:
        return ans
    elif index == 0:
        ans = nums[index]
        index += 1
        calculate(index,ans)
    else:
        for k in sign:
            if k != 0:
                if k == plus:
                    k -= 1
                    ans = sum(ans,nums[index])
                    calculate(index+1,ans)
                elif k == minus:
                    k -= 1
                    subtract(ans,nums[index])
                    calculate(index+1,ans)
                elif k == multiple:
                    k -= 1
                    multiply(ans,nums[index])
                    calculate(index+1,ans)
                elif k == division:
                    k -= 1
                    divide(ans,nums[index])
                    calculate(index+1,ans)
data = []
tmp = calculate(0,0)
data.append(tmp)
print(data)
print(min(data))