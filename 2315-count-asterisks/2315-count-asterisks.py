class Solution:
    def countAsterisks(self, s: str) -> int:
        ast = 0
        count = 0
        for item in s:
            if item == '|':
                count += 1
            if count %2 == 0:
                if item == '*':
                    ast += 1
        return ast
                    
            