from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        hmap = defaultdict(List)
    
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
    
            key = tuple(counts)
            if key in hmap:
                hmap[key].append(s)
            else:
                hmap[key] = [s]
            
        return hmap.values()

"""       
        hmap = defaultdict(List)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in hmap:
                hmap[sorted_s] = [s]
            else:
                hmap[sorted_s].append(s)
        return hmap.values()
        
"""