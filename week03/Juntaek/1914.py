def f(n, _from, temp, _to):
    if(n == 1):
        print(_from, _to, sep = " ")
    else:
        f(n-1, _from, _to, temp)
        f(1, _from, temp, _to)
        f(n-1, temp, _from, _to)

n = int(input())
print(2**n - 1)
if(n <= 20):
    f(n, 1, 2, 3)