class Solution:
    def replaceDigits(self, s: str) -> str:
        out = ""
        for item in s:
            if item.isalpha():
                out += item
            else:
                out += chr(ord(out[-1])+int(item))
        return out