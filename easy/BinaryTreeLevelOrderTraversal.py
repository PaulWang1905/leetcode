# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst = []
        if root:
            queue = [root]
            while queue:
                tmp, temp, ele = queue, [], []
                while tmp:
                    top = tmp.pop(0)
                    ele.append(top.val)
                    if top.left:
                        temp.append(top.left)
                    if top.right:
                        temp.append(top.right)
                if ele:
                    rst.append(ele)
                queue = temp
        return rst
