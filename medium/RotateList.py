# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p, n = head, 0
        if not p:
            return head
        while p:
            p = p.next
            n += 1
        p = head
        for i in range(n - k%n - 1):
            p = p.next
        new = ListNode(0)
        new.next, p.next = p.next, None
        q = new
        while q.next:
            q = q.next
        q.next = head
        return new.next
