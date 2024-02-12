class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 1
        l = 1
        
        while r < len(nums):
            if nums[r] == nums[r-1]:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
        return l