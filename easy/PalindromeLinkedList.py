# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        slow = self.reverse(slow)
        while slow and slow.val == head.val:
            slow = slow.next
            head = head.next
        return slow == None
        
    def reverse(self, head):
        rvs = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = rvs
            rvs = cur
            cur = temp
        return rvs
