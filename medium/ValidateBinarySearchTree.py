# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            stack, rst = [root], []
            p = root.left
            while p or stack:
                if p:
                    stack.append(p)
                    p = p.left
                else:
                    p = stack.pop()
                    if rst == []:
                        rst.append(p.val)
                    else:
                        if p.val > rst[-1]:
                            rst.append(p.val)
                        else:
                            return False
                    p = p.right
            return True
        return True
