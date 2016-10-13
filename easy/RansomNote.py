class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        rsmDict, mgzDict = Counter(ransomNote), Counter(magazine)
        if len(rsmDict) > len(mgzDict):
            return False
        for key in rsmDict:
            if key not in mgzDict or rsmDict[key] > mgzDict[key]:
                return False
        return True
