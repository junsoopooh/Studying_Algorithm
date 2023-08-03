import sys
sys.setrecursionlimit(10**6)

arr=[]
while True:
    try:
        num=int(sys.stdin.readline())
        arr.append(num)
    except:
        break
def search(left,right):
    if left>right:
        return
    else:
        mid=right+1
        for i in range(left+1,right+1):
            if arr[left]<arr[i]:
                mid=i
                break
        search(left+1,mid-1)
        search(mid,right)
        print(arr[left])

search(0,len(arr)-1)