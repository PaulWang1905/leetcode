class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_s, hash_t = {}, {}
        m, n = 0, 0
        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = m
                m += 1
                if t[i] not in hash_t:
                    hash_t[t[i]] = n
                    n += 1
                else:
                    return False
            else:
                if t[i] in hash_t:
                    if hash_t[t[i]] != hash_s[s[i]]:
                        return False
                else:
                    return False
        return True
