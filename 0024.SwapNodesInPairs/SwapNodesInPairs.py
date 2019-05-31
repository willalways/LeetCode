# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: return head
        ret = head.next
        head.next = self.swapPairs(ret.next)
        ret.next = head
        
        return ret
'''


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        ret = head.next
        head.next = ret.next
        ret.next = head

        while head.next != None and head.next.next != None:
            tmp = head.next.next
            head.next.next = tmp.next
            tmp.next = head.next
            head.next = tmp
            head = head.next.next
        return ret
