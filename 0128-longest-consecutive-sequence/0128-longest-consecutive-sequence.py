class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest = 0
        
        for num in nums:
            #if there is not a left value
            if num - 1 not in hset:
                length = 0
                while num + length in hset:
                    length += 1
                longest = max(longest,length)
        return longest