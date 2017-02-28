class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        kb = [
                ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                ['z', 'x', 'c', 'v', 'b', 'n', 'm']
            ]
        wordDict, rst = {}, []
        for i in range(len(kb)):
            for j in range(len(kb[i])):
                wordDict[kb[i][j]] = i
                
        for word in words:
            flag = True
            temp = list(word.lower())
            n = wordDict[temp[0]]
            for j in range(1, len(temp)):
                if n != wordDict[temp[j]]:
                    flag = False
                    break
            if flag:
                rst.append(word)
        return rst
