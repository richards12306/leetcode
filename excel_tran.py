
#!/usr/bin/python3
#-*- coding=utf-8 -*-

class Solution:
    def titleToNumber(self, s: str) -> int:
        value=0
        for i in range(len(s)):
            value = value + (ord(s[len(s) - 1 - i]) - 64) * 26**i
        return value


solute=Solution()
s=input()
print(solute.titleToNumber(s))