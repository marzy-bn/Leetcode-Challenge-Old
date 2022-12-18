class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = sorted(nums)
        hmap = {}
        for key,val in enumerate(lst):
            if val not in hmap:
                hmap[val] = key
        
        output = []
        for num in nums:
            output.append(hmap[num])
        return output