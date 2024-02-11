class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            if num in hmap:
                hmap[num] = 2
            else:
                hmap[num] = 1
                
        for key,val in hmap.items():
            if val == 1:
                return key