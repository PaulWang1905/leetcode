class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = s.split(' ')
        for i in range(len(tmp))[::-1]:
            if tmp[i] != '':
                return len(tmp[i])
        return 0
