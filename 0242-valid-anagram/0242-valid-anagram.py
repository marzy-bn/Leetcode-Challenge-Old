class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s)==sorted(t) 
    
        """
        if len(s) != len(t):
            return False
        
        hmap = {}
        
        for letter in s:
            if letter not in hmap:
                hmap[letter] = 1
            else:
                hmap[letter] += 1
        
        #print(hmap)
        
        for letter in t:
            if letter not in hmap:
                return False
            else:
                hmap[letter] -= 1
            if hmap[letter] == 0:
                del hmap[letter]
        
        return True
        """