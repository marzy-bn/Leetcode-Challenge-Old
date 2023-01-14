class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hmap = {}
        
        #creating a map
        for t in target:
            if t in hmap:
                hmap[t] += 1
            else:
                hmap[t] = 1
        
        for a in arr:
            if a in hmap and hmap[a] > 0:
                hmap[a] -= 1
            else:
                return False
        return True