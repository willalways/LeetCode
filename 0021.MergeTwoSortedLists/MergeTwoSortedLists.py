# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l2 == None:
            return l1
        if l1 == None:
            return l2
        if l1.val <= l2.val:
            ret = l1
            l1 = l1.next
        else:
            ret = l2
            l2 = l2.next
        p = ret
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l2 == None:
            p.next = l1
        if l1 == None:
            p.next = l2
        return ret
