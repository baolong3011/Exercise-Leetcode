class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.lower().split()
        res = []
        for word in words:
            if len(word) <= 2:
                res.append(word.lower())
            else:
                res.append(word[0].upper() + word[1:].lower())
        return ' '.join(res)