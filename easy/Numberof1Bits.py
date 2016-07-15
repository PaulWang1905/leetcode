class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #return bin(n).count('1')
        string, cnt = bin(n), 0
        for i in string:
            if i == '1':
                cnt += 1
        return cnt
