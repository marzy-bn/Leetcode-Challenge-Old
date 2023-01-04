class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = {}
        for num in arr:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
        return len(hmap.values()) == len(set(hmap.values()))