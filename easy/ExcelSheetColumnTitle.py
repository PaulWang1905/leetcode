class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        rst = ''
        if n <= 0:
            return rst
        
        tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        while n > 0:
            tmp = n % 26
            n = (n - 1) / 26
            rst += tab[tmp - 1]
        
        return rst[::-1]
