class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        for idx, num in enumerate(nums):
            if target - num not in hmap:
                hmap[num] = idx
            else:
                return [idx,hmap[target-num]]
        