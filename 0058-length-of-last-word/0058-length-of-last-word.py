class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(' ')
        word = s.split(' ')[-1]
        return len(word)