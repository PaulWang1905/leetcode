'''
using zip
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A, low = [], n*n+1
        while low > 1:
            high = low
            low -= len(A)
            A = [list(range(low, high))] + list(zip(*A[::-1]))
        return A
