# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, p = head, head.next
        first = p
        while pre and p:
            tmp = pre
            pre.next = p.next
            p.next = pre
            if pre.next and pre.next.next:
                pre = pre.next
                p = pre.next
                tmp.next = p
            else:
                break
        return first 
