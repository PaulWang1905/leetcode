class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        chDict = {}
        for ch in s:
            if ch not in chDict:
                chDict[ch] = 1
            else:
                chDict[ch] += 1
        chList = sorted(chDict.items(), key=lambda x: x[1], reverse=True)
        res = ''
        for element in chList:
            res += element[0] * element[1]
        return res
