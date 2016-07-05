class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash1, hash2 = {}, {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] not in hash1.keys():
                    hash1[s[i]] = 1
                else:
                    hash1[s[i]] += 1
                if t[i] not in hash2.keys():
                    hash2[t[i]] = 1
                else:
                    hash2[t[i]] += 1
            if hash1 == hash2:
                return True
        return False
