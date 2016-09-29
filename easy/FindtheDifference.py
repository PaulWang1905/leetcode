class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        m, n = Counter(s), Counter(t)
        for k in n:
            if k in m:
                if m[k] != n[k]:
                    return k
            else:
                return k
