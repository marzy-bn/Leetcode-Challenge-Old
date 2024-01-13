class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #[2,7,11,15]
        #{2:0,7:1,11:2,15:3}
        
        hmap = {}
        for idx,num in enumerate(nums):
            hmap[num]=idx
        for idx,num in enumerate(nums):
            complement = target - nums[idx]
            if complement in hmap and hmap[complement] != idx:
                return idx,hmap[complement]
                
                
        