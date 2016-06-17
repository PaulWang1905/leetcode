class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rst = int(repr(x)[::-1]) if x >= 0 else int('-' + repr(x)[1:][::-1])
        return 0 if abs(rst) >= 2147483647 else rst
