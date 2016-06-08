# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = ListNode(0)
        p = odd
        even = ListNode(0)
        q = even
        while head:
            p.next = head
            p = p.next
            if head.next:
                q.next = head.next
                q = q.next
                head = head.next.next
            else:
                break
        q.next = None
        p.next = even.next
        return odd.next
