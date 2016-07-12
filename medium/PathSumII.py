# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack, rst = [(root, [root.val])], []
        while stack:
            top, value = stack.pop()
            if not top.left and not top.right:
                if sum(value) == sum1:
                    rst.append(value)
            if top.right:
                stack.append((top.right, value + [top.right.val]))
            if top.left:
                stack.append((top.left, value + [top.left.val]))
        return rst
