import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = int(input().rstrip())
c = int(input().rstrip())

str_mul = str(a*b*c)

index_list = [0]*10
for e in str_mul:
    index_list[int(e)] += 1

print(*index_list, sep='\n')