# # ( ) 이렇게 되면 2
# # [] 이렇게 되면 3
# # ([]) 이렇게 되면 6
# # (()) 이렇게 되면 4
# # [[]] 이렇게 되면 9
# # ()[] 이렇게 되면 더하기

# data = input().rstrip()
# ret = []
# count = 0
# for i in data:
#     # print(i)
    
#     if len(ret) == 0:
#         if i == '(' or '[':
#             ret.append(i)
#         else:
#             break
#     else:
#         if ret[-1] == '(':
#             if i == '(':
#                 ret.append(i)
#                 count *= 2
#             elif i == ')':
#                 ret.pop()
#                 count += 2
#             elif i == '[':
#                 ret.append(i)
#             else:
#                 break
#         if ret[-1] == '[':
#             if i == '[':
#                 ret.append(i)
#                 count *= 3
#             elif i == ']':
#                 ret.pop()
#                 count += 3
#             elif i == '(':
#                 ret.append()
#             else:
#                 break
# print(ret)
# print(count)
            
    
word = input()
l = []
result = 0
n = 1

for i in range(len(word)):
    if word[i] == '(':
        l.append('(')
        n *= 2
    elif word[i] == '[':
        l.append('[')
        n *= 3
    elif word[i] == ')':
        if not l or l[-1] != '(':
            result = 0
            break
        if word[i-1] == '(':
            result += n
        l.pop()
        n //= 2
    elif word[i] == ']':
        if not l or l[-1] != '[':
            result = 0
            break
        if word[i-1] == '[':
            result += n
        l.pop()
        n //= 3
if l:
    result = 0
print(result)
