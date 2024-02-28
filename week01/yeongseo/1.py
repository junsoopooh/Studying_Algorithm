# def solution(n):
#     n = list(str(n))

#     def quick(arr):
#         if len(arr) == 1 or len(arr) == 0:
#             return arr

#         pivot = 0

#         left = []
#         right = []

#         for i in range(1, len(arr)):
#             if arr[i] > arr[pivot]:
#                 left.append(arr[i])
#             else:
#                 right.append(arr[i])

#         return quick(left) + [arr[pivot]] + quick(right)

#     ans = quick(n)
#     return int("".join(ans))

def solution(arr):
    arr = list(str(arr))
    
    def in_place_quick_sort(start, end):
        if end <= start:
            return 
        
        mid = partition(start, end) # 분할의 기준점 
        in_place_quick_sort(start, mid -1)
        in_place_quick_sort(mid, end)
        
    def partition(lo, hi):
        pivot = arr[(lo + hi) // 2]  # 대소 비교를 위한 pivot 값
        while lo <= hi:
            while arr[lo] > pivot:
                lo += 1
            while arr[hi] < pivot:
                hi -= 1
            if lo <= hi:
                arr[lo], arr[hi] = arr[hi], arr[lo]
                lo += 1
                hi -= 1
        
        return lo 
            
    in_place_quick_sort(0, len(arr) - 1)
    return int("".join(arr))

solution(118372)
    

        