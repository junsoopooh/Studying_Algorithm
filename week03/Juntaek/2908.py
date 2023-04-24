# num_data = input().split()
# print(num_data)
# num1 = list(num_data[0])
# num2 = list(num_data[1])
# num1.reverse()
# num2.reverse()
# ''.join(num1)
# ''.join(num2)
# if int(num1) > int(num2):
#     print(int(num1))
# else:
#     print(int(num2))
A, B = input().split()
reverse_A = int(A[::-1])
reverse_B = int(B[::-1])
if reverse_A > reverse_B:
    print(reverse_A)
else:
    print(reverse_B)