# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst = []
        queue = [root]
        q = []
        while queue or q != []:
            if q != []:
                queue = q
                q = []
            tmp = []
            while queue:
                now = queue.pop(0)
                if now:
                    tmp.append(now.val)
                    q.append(now.left)
                    q.append(now.right)
            if tmp != []:
                rst.append(tmp)
        return rst[::-1]
