class Solution:
    def romanToInt(self, s: str) -> int:
        r_i = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if r_i[s[i]] >= r_i[s[i+1]]:
                total += r_i[s[i]]
            else:
                total -= r_i[s[i]]
                
        return total + r_i[s[len(s) - 1]]