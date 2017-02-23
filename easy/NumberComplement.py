class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a, res = bin(num), ''
        for i in range(2, len(a)):
            if a[i] == '1':
                res += '0'
            else:
                res += '1'
        return int(res, base=2)
