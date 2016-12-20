class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bix, biy = bin(x)[2:], bin(y)[2:]
        if len(bix) > len(biy):
            biy = (len(bix) - len(biy)) * '0' + biy
        else:
            bix = (len(biy) - len(bix)) * '0' + bix
        cnt = 0
        for i in range(len(bix)):
            if bix[i] != biy[i]:
                cnt += 1
        return cnt
