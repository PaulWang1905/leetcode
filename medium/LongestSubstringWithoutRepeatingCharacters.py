class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hsmap = {}
        cnt = left = 0
        for i in range(len(s)):
            if s[i] in hsmap:
                cnt = max(cnt, i - left)
                left = max(left, hsmap[s[i]] + 1)
            hsmap[s[i]] = i
        return max(cnt, len(s) - left)
