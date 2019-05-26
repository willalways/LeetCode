# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not n: return head
        start,end,step = head,head,n
        while step > 0 and end.next != None:
            end = end.next
            step -= 1
        if step == 0:
            while end.next != None:
                start,end = start.next, end.next
            start.next = start.next.next
        else:
            head = head.next
        return head
        