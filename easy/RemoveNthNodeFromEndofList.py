# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p, cnt = head, 0
        while p:
            p = p.next
            cnt += 1
        
        if n == cnt:
            return head.next
        
        p = head
        for i in range(cnt - n - 1):
            p = p.next
        p.next = p.next.next
        return head
