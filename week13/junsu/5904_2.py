import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
# legnth는 문자열의 길이, i는 차수
def search(k,length,i):
    if k == 1:
        print('m')
        return
    elif k == 2 or k == 3:
        print('o')
        return

    next_length = 2*length+i+3
    if k > next_length:
        search(k,next_length,i+1)
    else:
        if k > length and k <= i+3+length:
            if k - length == 1:
                print('m')
            else:
                print('o')
            return
        else:
            k -= (length+i+3)
            search(k,3,1)

search(n,3,1)