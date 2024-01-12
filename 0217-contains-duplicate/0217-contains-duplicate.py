class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hmap = set()
        
        for num in nums:
            if num not in hmap:
                hmap.add(num)
            else:
                return True
        return False