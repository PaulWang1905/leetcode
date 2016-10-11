class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, cnt = 0, 0
        flag = False
        for i in range(len(s)):
            for j in range(m, len(t)):
                if s[i] == t[j]:
                    m = j + 1
                    cnt += 1
                    break
                if j+1 == len(t):
                    return False
        return True if cnt == len(s) else False
