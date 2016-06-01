class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        stc = str.split()
        if len(stc) != len(pattern):
            return False
        ptHash = {}
        stHash = {}
        for i in range(len(stc)):
            if pattern[i] not in ptHash:
                ptHash[pattern[i]] = stc[i]
            else:
                if ptHash[pattern[i]] != stc[i]:
                    return False
            if stc[i] not in stHash:
                stHash[stc[i]] = pattern[i]
            else:
                if stHash[stc[i]] != pattern[i]:
                    return False
        return True
