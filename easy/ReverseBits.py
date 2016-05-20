class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bi = bin(n)[2:]
        if len(bi) < 32:
            bi = '0' * (32 - len(bi)) + bi
        return int(bi[::-1], 2)
