# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst = []
        if root:
            rst = [[root.val]]
        else:
            return rst
        queue, flag = [root], False
        while queue:
            tmp = []
            for i in range(len(queue)):
                top = queue.pop(0)
                if top.left:
                    tmp.append(top.left)
                if top.right:
                    tmp.append(top.right)
            res = []
            if flag:
                for ele in tmp:
                    res.append(ele.val)
            else:
                for ele in tmp[::-1]:
                    res.append(ele.val)
            rst.append(res)
            queue, flag = tmp, not flag
        return rst[:-1]
