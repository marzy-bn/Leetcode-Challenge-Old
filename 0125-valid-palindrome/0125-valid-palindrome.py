class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = ''
        for char in s:
            if char.isalnum():
                new_s += char
        new_s = new_s.lower()
        print(new_s)
        i = 0
        j = len(new_s)-1
        while i<(len(new_s)//2):
            if new_s[i] != new_s[j]:
                return False
            i+=1
            j-=1
        return True
                        
                