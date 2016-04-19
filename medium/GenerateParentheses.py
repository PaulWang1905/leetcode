'''
recursive method
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        else:
            L = self.generateParenthesis(n-1)
            L1 = []
            for i in L:
                i += ")"
                for j in range(len(i)):
                    if i[j] == ")":
                        L1.append(i[:j] + "(" + i[j:])
        L2 = list(set(L1))
        return L2
