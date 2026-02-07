class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        i = len(needle)
        j = len(haystack)
        for k in range(j - i + 1):
            if haystack[ k : k + i ] == needle:
                return k
    
        return -1