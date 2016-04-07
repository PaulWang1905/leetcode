'''
binary search
'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low < high:
            tmp = (low + high) / 2
            if isBadVersion(tmp):
                high = tmp
            else:
                low = tmp + 1
        return low
