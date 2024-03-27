k , n = map(int, input().split())
lengths = [int(input()) for _ in range(k)]

def count(cut_standard, lengths):
    ans = 0 
    for i in lengths:
        ans += i // cut_standard
    
    return ans

lo = 1
hi = max(lengths)

while lo <= hi:
    mid = (lo + hi) // 2

    if count(mid, lengths) >= n:
        lo = mid + 1
    else:
        hi = mid - 1
    
print(hi)