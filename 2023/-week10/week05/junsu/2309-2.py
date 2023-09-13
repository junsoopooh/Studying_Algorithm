import sys

dwarfs = []
for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))

total = sum(dwarfs)
num = total - 100 

def search(dwarfs,num):
    for i in range(8): 
        for j in range(i+1,9):
            if dwarfs[i] + dwarfs[j] == num:
                a = dwarfs[i]
                b = dwarfs[j]
                dwarfs.remove(a)
                dwarfs.remove(b)
                return

search(dwarfs,num)
dwarfs.sort()
print(*dwarfs, sep='\n')