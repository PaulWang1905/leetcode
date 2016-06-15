# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # recursive
        #return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

        # stack
        rst = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                rst.append(tmpNode.val)
                root = tmpNode.right
        return rst
