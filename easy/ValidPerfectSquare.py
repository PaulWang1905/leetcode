class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i, j = 1, 1
        while i < num:
            j += 2
            i += j
        return i == num
