class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
        out = 0
        for val in hmap.values():
            out += val * (val - 1) // 2
        return out