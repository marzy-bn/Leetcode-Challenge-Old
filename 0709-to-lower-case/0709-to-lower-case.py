class Solution:
    def toLowerCase(self, s: str) -> str:
        out = ''
        for letter in s:
            if ord(letter) <= 90 and ord(letter) >= 65:
                out += chr(ord(letter) + 32)
            else:
                out += letter
        return out