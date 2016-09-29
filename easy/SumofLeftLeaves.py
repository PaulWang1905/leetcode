# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack, binary = [root], [0]
        rst = []
        while stack:
            p, q = stack.pop(0), binary.pop(0)
            if p.left:
                stack.append(p.left)
                binary.append(1)
            if p.right:
                stack.append(p.right)
                binary.append(0)
            if not p.left and not p.right:
                if q == 1:
                    rst.append(p.val)
                    
        return sum(rst)
