# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def merge2list(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        if left.val < right.val:
            cur = left
            left = left.next
        else:
            cur = right
            right = right.next
        ret = cur
        while left != None and right != None:
            if left.val < right.val:
                cur.next = left
                left = left.next
                cur = cur.next
            else:
                cur.next = right
                right = right.next
                cur = cur.next
        if left == None:
            cur.next = right
        else:
            cur.next = left
        return ret

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        listlen = len(lists)
        if listlen == 0:
            return None
        if listlen == 1:
            return lists[0]
        if listlen == 2:
            return self.merge2list(lists[0], lists[1])
        left = self.mergeKLists(lists[0:listlen//2])
        right = self.mergeKLists(lists[listlen//2:listlen])
        return self.merge2list(left, right)
