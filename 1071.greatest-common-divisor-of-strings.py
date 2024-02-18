class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        a = len (str1)
        b = len (str2)

        c =""
        if ((a == b) & (str1 != str2)) :
            return (c)

        
        e = a//b
        if (e*str2) == str1:
            return str2
        for d in range(1,b):
            c = str2[:-d]
            f = len (c)
            if f == 0:
                return ""
            e = a//f
            h = b//f
            if (((e*c) == str1) & ((h*c) == str2)):
                return c
        return ""