import sys
input = sys.stdin.readline

S1, S2 = input().rstrip().split()

S1_r = int(S1[2] + S1[1] + S1[0])
S2_r = int(S2[2] + S2[1] + S2[0])

print(S1_r) if S1_r > S2_r else print(S2_r)