# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        if head == None:
            return None
        tmp = []
        i = 0
        for i in range(k):
            if head != None:
                tmp.append(head)
                head = head.next
        if len(tmp) < k:
            return tmp[0]
        ret = tmp.pop()
        recursion, cur = ret.next, ret
        for i in range(k - 1):
            cur.next = tmp.pop()
            cur = cur.next
        cur.next = self.reverseKGroup(recursion, k)
        return ret
