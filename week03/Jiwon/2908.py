import sys
input = sys.stdin.readline

a, b = map(int, input().split())

a_reverse = (a % 10) * 100 + (a % 100 - a % 10) + (a // 100)
b_reverse = (b % 10) * 100 + (b % 100 - b % 10) + (b // 100)

print(a_reverse if a_reverse > b_reverse else b_reverse)