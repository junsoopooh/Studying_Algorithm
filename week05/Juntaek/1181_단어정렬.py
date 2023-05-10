n = int(input())
data = []
for _ in range(n):
    data.append(input())
# print(data)
# data.sort(key=len, x: lambda)
result1 = set(data)
result1 = list(result1)
# print(result1)
result1.sort()
result2  = sorted(result1, key=lambda x: len(x))
# print(result2)
for ret in result2:
    print(ret)