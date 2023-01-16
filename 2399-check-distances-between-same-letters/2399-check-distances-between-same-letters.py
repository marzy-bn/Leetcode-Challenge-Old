class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hmap = {}
        for idx,char in enumerate(s):
            if char not in hmap:
                hmap[char] = idx
            else:
                hmap[char] = idx - hmap[char] - 1
        print(hmap)
        i = 97
        idx = 0
        while i <= 122: 
            if chr(i) in hmap.keys() and distance[idx]!=hmap[chr(i)]:
                return False
            i += 1
            idx += 1
        return True