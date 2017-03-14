class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        rst = ''
        for i in xrange(0, len(s), 2*k):
            rst += s[i:i+k][::-1] + s[i+k:i+2*k]
        return rst
