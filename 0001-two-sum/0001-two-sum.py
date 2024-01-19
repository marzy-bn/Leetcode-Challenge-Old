class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        for idx,num in enumerate(nums):
            hmap[num] = idx
        
        for idx,num in enumerate(nums):
            if target - num in hmap and hmap[target-num] != idx:
                return idx,hmap[target-num]