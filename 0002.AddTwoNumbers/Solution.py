# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        start = ListNode(0)
        end = start
        while l1 != None or l2 != None or carry != 0:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            newnode = ListNode(0)
            newnode.val = l1.val + l2.val + carry
            carry = newnode.val // 10
            newnode.val %= 10
            end.next = newnode
            end = newnode
            l1 = l1.next
            l2 = l2.next
        return start.next
