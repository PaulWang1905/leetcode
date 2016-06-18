# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            rst = [root.val]
        else:
            return []
        queue = [root]
        while queue:
            tmp = []
            for i in range(len(queue)):
                q = queue.pop(0)
                if q.left:
                    tmp.append(q.left)
                if q.right:
                    tmp.append(q.right)
            if tmp:
                rst.append(tmp[-1].val)
            queue = tmp
        return rst
