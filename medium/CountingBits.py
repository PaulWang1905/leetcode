class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        rst = [0]
        while len(rst) <= num:
            rst += [i+1 for i in rst]
        return rst[:num+1]
