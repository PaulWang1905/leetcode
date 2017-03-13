# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))
    
    def dfs(self, root):
        if not root:
            return (0, 0)
        left, right = self.dfs(root.left), self.dfs(root.right)
        now = root.val + left[1] + right[1]
        later = max(left) + max(right)
        
        return (now, later)
