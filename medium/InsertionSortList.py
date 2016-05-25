# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, tmp = head, []
        while p:
            tmp.append(p.val)
            p = p.next
        tmp.sort()
        p = head
        for t in tmp:
            p.val = t
            p = p.next
        return head
