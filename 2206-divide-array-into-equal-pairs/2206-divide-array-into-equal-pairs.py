class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hmap = {}
        for num in nums:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
        for key,val in hmap.items():
            if val%2!=0:
                return False
        return True