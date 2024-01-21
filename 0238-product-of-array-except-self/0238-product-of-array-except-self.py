class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)
        
        p = 1
        for i in range(len(nums)):
            result[i] = p
            p *= nums[i]
        #1 1 2 6
        p = 1
        for j in range(len(nums)-1,-1,-1):
            result[j] *= p
            p *= nums[j]
        
        return result
            
            
            
            
            
            
            