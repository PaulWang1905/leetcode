# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        stack, res = [(root, [str(root.val)])], []
        while stack:
            temp, val = stack.pop()
            if not temp.left and not temp.right:
                res.append('->'.join(val))
            if temp.left:
                stack.append((temp.left, val + [str(temp.left.val)]))
            if temp.right:
                stack.append((temp.right, val + [str(temp.right.val)]))
        return res
