'''
use dictionary to store each ans
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        uniqueTree = {0: 1, 1: 1}
        
        for i in range(2, n+1):
            tmp = 0
            for j in range(i):
                tmp += uniqueTree[j] * uniqueTree[i-j-1]
            uniqueTree[i] = tmp
        
        return uniqueTree[n]
