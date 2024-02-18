class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w3 = ""
        a = len(word1)
        b = len(word2)
        c = max(a,b)
        d = 0
        if a == b:
            while d < c:
                t = ""
                t = word1[d] + word2[d]
                w3 +=t
                d+=1
        elif a < b:
            while d < a:
                t = ""
                t = word1[d] + word2[d]
                w3 +=t
                d+=1
            if d < b:
                t = word2[d:b]
                w3+=t
        elif a > b:
            while d < b:
                t = ""
                t = word1[d] + word2[d]
                w3 +=t
                d+=1
            if d < a:
                t = word1[d:a]
                w3+=t
        return w3
