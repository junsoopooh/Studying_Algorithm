# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        def solve(head,val):
            #범위를 벗어나지 않게.
            if head and head.next : 
                if head.next.val == val :
                    if head.next.next == None :
                        head.next = None
                    else:
                        head.next = head.next.next
                    solve(head,val)
                else : 
                    solve(head.next,val)
        #처음 들어온 값들이 val과 같은 값인 경우.
        while head and head.val == val : 
            head = head.next
        res = head
        solve(head,val)
        return res