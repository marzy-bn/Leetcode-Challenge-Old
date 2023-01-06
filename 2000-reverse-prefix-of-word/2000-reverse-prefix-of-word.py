class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pref = ""
        for idx,let in enumerate(word):
            if let != ch:
                pref += let
            elif let == ch:
                pref += let
                return pref[::-1] + word[idx+1:]
        return word