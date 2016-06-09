class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        rev = []
        idx = []
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(l)):
            if l[i] in vowels:
                rev.append(l[i])
                idx.append(i)
        val = 0
        while len(rev) > 0:
            l[idx[val]] = rev.pop()
            val += 1
        return ''.join(l)
