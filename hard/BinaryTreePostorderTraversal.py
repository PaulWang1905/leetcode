# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rst, stack = [], [[root, 1]]
        while stack:
            tmp, cnt = stack[-1]
            if (not tmp.right and not tmp.left) or cnt == 0:
                rst.append(tmp.val)
                stack.pop()
            else:
                stack[-1][1] -= 1
                if tmp.right:
                    stack.append([tmp.right, 1])
                if tmp.left:
                    stack.append([tmp.left, 1])
        return rst
