class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hset = set()
        for char in s:
            if char not in hset:
                hset.add(char)
            else:
                return char