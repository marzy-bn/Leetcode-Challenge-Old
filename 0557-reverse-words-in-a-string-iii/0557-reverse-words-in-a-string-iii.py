class Solution:
    def reverseWords(self, s: str) -> str:
        out = ''
        for word in s.split():
            out += word[::-1] + ' '
        return out.rstrip()
            