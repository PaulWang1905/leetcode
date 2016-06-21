# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        queue = [root]
        while queue:
            tmp, n = [], len(queue)
            for i in range(n):
                top = queue[i]
                if top.left:
                    tmp.append(top.left)
                if top.right:
                    tmp.append(top.right)
                if i == n - 1:
                    top.next = None
                else:
                    top.next = queue[i + 1]
            queue = tmp
