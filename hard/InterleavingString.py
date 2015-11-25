'''
method: use matrix
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        pre = ListNode(0)
        cur = ListNode(0)
        
        p.next = head
        cur = p
        pre = head
        
        
        while pre:
            isDup = False
            while pre.next != None and pre.val == pre.next.val:
                isDup = True
                pre = pre.next
            if isDup:
                pre = pre.next
                continue
            cur.next = pre
            cur = cur.next
            pre = pre.next
        cur.next = pre
        return p.next
