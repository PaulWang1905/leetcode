'''
Binary method
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a = dividend
        b = divisor
        isPositive, a, b, res = (a >= 0) ^ (b < 0), abs(a), abs(b), 0
        while a >= b:
            n, nb = 1, b
            while a >= nb:
                a, res = a - nb, res + n
                n, nb = n << 1, nb << 1
        return min(res, 2147483647) if isPositive else max(-res, -2147483648)
