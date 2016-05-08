class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        binary = bin(num)[2:]
        if len(binary) % 2 == 1 and binary.replace('0', '') == '1':
            return True
        return False
