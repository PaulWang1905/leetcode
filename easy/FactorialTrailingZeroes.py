'''
method: the result equals the number of 5 from 1 to n
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        res = 0
        while n >= x:
            res += n/x
            x *= 5
        
        return res
