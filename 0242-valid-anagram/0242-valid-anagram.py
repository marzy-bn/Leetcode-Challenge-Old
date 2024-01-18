class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap1 = {}
        hmap2 = {}
        for item in s:
            hmap1[item] = hmap1.get(item,0) + 1
        for item in t:
            hmap2[item] = hmap2.get(item,0) + 1
        
        return hmap1 == hmap2
            
            