class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        count = 0
        i = 0
        while i < len(s):
            if s[i] == 'R':
                count += 1
                i += 1
            elif s[i] == 'L':
                count -= 1
                i += 1
            if count == 0:
                total += 1
        return total
                
                
            