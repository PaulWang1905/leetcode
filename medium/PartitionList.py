# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        former, latter = ListNode(0), ListNode(0)
        f = former
        l = latter
        
        while head:
            if head.val < x:
                f.next = head
                f = f.next
            else:
                l.next = head
                l = l.next
            head = head.next
        
        l.next = None
        f.next = latter.next
        return former.next
