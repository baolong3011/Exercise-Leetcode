class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        p1 = 0
        p2 = 0
        n = len(s)
        k = len(t)
        while p2 < k:
            if t[p2] == s[p1]:
                p1 += 1
            p2 += 1
            if p1 == n:
                return True
        return False