'''
method: idetify string is legal or not
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max = 2147483647
        min = -2147483648
        
        if len(str) == 0:
            return 0
        
        str = str.lstrip()
        if str == '':
            return 0
        
        i = 0
        signal = 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            signal = -1
        
        res = 0
        for j in range(i, len(str)):
            if str[j]>='0' and str[j]<='9':
                res = res*10 + ord(str[j])-ord('0')
                i += 1
            else:
                break
        
        res = res*signal
        if res > max:
            res = max
        elif res < min:
            res = min
        
        return res
