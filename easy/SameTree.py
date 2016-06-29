# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            a, b = [p], [q]
            while a and b:
                t1, t2 = a.pop(0), b.pop(0)
                if t1.val == t2.val:
                    if t1.left and t2.left:
                        a.append(t1.left)
                        b.append(t2.left)
                    elif t1.left or t2.left:
                        return False
                    if t1.right and t2.right:
                        a.append(t1.right)
                        b.append(t2.right)
                    elif t1.right or t2.right:
                        return False
                else:
                    return False
            if a == b:
                return True
            return False
        elif p or q:
            return False
        return True
