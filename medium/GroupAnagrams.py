'''
use map method
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d,res= {},[]
        for i in strs:
            sortstr = ''.join(sorted(i))
            if sortstr in d:
                d[sortstr] += [i]
            else:
                d[sortstr] = [i]
        
        for i in d:
            tmp = d[i]
            tmp.sort()
            res += [tmp]
        return res
