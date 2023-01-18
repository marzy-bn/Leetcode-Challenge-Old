class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        out = []
        i = 0
        while i < len(s)-2:
            sub = s[i:i+3]
            out.append(sub)
            i += 1
        count = 0
        for sub in out:
            if len(set(sub)) == 3:
                count += 1
        return count