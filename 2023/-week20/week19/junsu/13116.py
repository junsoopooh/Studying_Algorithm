import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    def main(x):
        arr = []
        while x > 1:
            arr.append(x)
            x //= 2
        return arr
    arr_a = main(a)
    arr_b = main(b)
    ans = []
    for x in arr_a:
        if x in arr_b:
            ans.append(x)
    if ans:
        print(10*max(ans))
    else:
        print(10)
