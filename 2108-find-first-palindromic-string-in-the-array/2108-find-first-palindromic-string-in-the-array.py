class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i = 0
            flag = 0
            while i < len(word)//2:
                if word[i] != word[len(word)-i-1]:
                    flag = 1
                    break
                i += 1
            if flag == 0:
                return word
        return ""
            