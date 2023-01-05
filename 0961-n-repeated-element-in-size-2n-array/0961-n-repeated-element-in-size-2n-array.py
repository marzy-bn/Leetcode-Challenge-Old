class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        p = len(nums)/2
        
        hmap = {}
        for num in nums:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
        
        for key,val in hmap.items():
            if val == p:
                return key