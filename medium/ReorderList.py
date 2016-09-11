# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return 
        
        # get length
        length, p = 0, head
        while p:
            length += 1
            p = p.next
        cur = head
        for i in range(length / 2):
            cur = cur.next
        print cur.val
        
        # reverse
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            
        # link
        while head.next and pre.next:
            tmp, temp = head.next, pre.next
            head.next = pre
            pre.next = tmp
            head, pre = tmp, temp
