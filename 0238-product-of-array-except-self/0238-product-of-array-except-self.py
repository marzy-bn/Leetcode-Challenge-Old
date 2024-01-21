class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = []
        post = [0] * len(nums)
        
        p = 1
        for i in range(len(nums)):
            pre.append(p)
            p *= nums[i]
        p = 1
        for j in range(len(nums)-1,-1,-1):
            post[j] = p
            p *= nums[j]
        result = []
        for i in range(len(nums)):
            result.append(pre[i]*post[i])
        return result
            
            
            
            
            
            
            