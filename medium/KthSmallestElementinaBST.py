# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        import bisect as bs
        queue = [root]
        rst = []
        while queue:
            head = queue.pop(0)
            if head:
                bs.insort(rst, head.val)
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
        return rst[k-1]
