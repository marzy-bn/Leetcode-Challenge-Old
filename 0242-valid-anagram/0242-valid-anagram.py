class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        hmap = {}
        for val in s:
            if val not in hmap:
                hmap[val] = 1
            else:
                hmap[val] += 1
                
        for val in t:
            if val not in hmap:
                return False
            else:
                hmap[val] -= 1
                if hmap[val] == 0:
                    del hmap[val]
        return True