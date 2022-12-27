class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        print(vowels)
        length = len(s)
        l = length//2
        left = 0
        right = 0
        for ch in s[0:l]:
            if ch in vowels:
                left += 1
        for ch in s[l:len(s)]:
            if ch in vowels:
                right += 1
        return left == right