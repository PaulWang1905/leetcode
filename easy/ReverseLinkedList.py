'''
method: once a position move
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''if head == None or head.next == None:
            return head
        '''
        p = ListNode(0)		
        while head:			
            next = head.next			
            head.next = p.next			
            p.next = head			
            head = next		
        return p.next
