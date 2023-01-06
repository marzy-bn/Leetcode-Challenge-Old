import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for item in s:
            if item == letter:
                count += 1
        out = (count / len(s)) * 100
        return math.trunc(out)