class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        hmap = {}
        out = []
        for i in nums:
            hmap[i] = nums[i]
        for num in nums:
            out.append(hmap[num])
        return out