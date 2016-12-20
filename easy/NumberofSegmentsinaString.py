class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # a-z: 97-122
        # A-Z: 65-90
        return len(filter(lambda x: x!='', s.split(' ')))
