class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        if s[-1][-1] != s[0][0]:
            return True
        for x in range(len(s)-1):
            if s[x][-1] != s[x+1][0]:
                return True
        return False
