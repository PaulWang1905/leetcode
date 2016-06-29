class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        if n == 2 or n == 3:
            return n - 1
        a, b = n / 3, n % 3
        if b == 0:
            return 3 ** a
        if b == 1:
            return 3 ** (a-1) * 4
        if b == 2:
            return 3 ** a * 2
