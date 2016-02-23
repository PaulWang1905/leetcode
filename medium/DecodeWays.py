'''
use dp[i-1] and dp[i-2] to generate dp[i]
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [1] + [0] * len(s)
        ok = lambda x: x[0] != '0' and  int(x) >= 1 and int(x) <= 26;
        for i in range(1, len(s) + 1):
            dp[i] = dp[i-1] if s[i-1] != '0' else 0
            if i >= 2:
                dp[i] += dp[i-2] if ok(s[i-2:i]) else 0
        return dp[len(s)]
