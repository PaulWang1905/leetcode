# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        queue = [root]
        while queue:
            tmp, temp = [], queue
            for i in range(len(temp) - 1):
                temp[i].next = temp[i+1]
                if temp[i].left:
                    tmp.append(temp[i].left)
                if temp[i].right:
                    tmp.append(temp[i].right)
            if temp[-1]:
                if temp[-1].left:
                    tmp.append(temp[-1].left)
                if temp[-1].right:
                    tmp.append(temp[-1].right)
            queue = tmp
