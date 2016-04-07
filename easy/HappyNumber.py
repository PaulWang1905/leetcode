class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = 0
        while(n != 1 and n != 4):
            while(n):
                num += (n%10) * (n%10)
                n /= 10
            n = num
            num = 0
        return 1 == n
