'''
method: S(n) = S(n-1)+S(n-2)
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        tmp = [1,2,0]
        for i in range(2, n):
            tmp[2] = tmp[1] + tmp [0]
            tmp[0],tmp[1] = tmp[1],tmp[2]
        return tmp[2]
