class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        st = ''
        for letter in s:
            if letter.isalnum():
                st += letter.lower()
        
        i = 0
        j = len(st) - 1
        while i < len(st)//2:
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1
        return True
                        
                
                