# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        '''
        left = ListNode(0)
        left.next = head
        pre = left
        for i in range(m - 1):
            pre = pre.next
        p = pre.next
        for i in range(n - m):
            cur = p.next
            p.next = cur.next
            cur.next = pre.next
            pre.next = cur
        return left.next
        '''
        pre, headt = head, None
        for i in range(m - 1):
            headt = pre
            pre = pre.next
        for i in range(n - m):
            cur = pre.next
            pre.next = cur.next
            if headt != None:
                cur.next = headt.next
                headt.next = cur
            else:
                cur.next = head
                head = cur
        return head
