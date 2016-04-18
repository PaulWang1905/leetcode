'''
filter ''
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return s
        
        rst = s.split(' ')
        rst = filter(lambda x: x != '', rst)
        rst.reverse()
        return ' '.join(rst)
