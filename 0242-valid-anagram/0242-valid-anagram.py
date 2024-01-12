class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}
        hmap2 = {}
        for num in s:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
        
        for num in t:
            if num not in hmap2:
                hmap2[num] = 1
            else:
                hmap2[num] += 1
        
        return hmap == hmap2
            